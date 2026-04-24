# Jenkins Agent Backup

This directory stores the files needed to recreate a local Jenkins inbound agent without committing the live runtime directory from `/home/mniedziolka/jenkins-agent`.

What is versioned here:

- `run_jenkins_agent.sh`: downloads `agent.jar` and runs the local inbound agent process.
- `.env.example`: template for controller URL and agent credentials.
- `.gitignore`: keeps runtime files and secrets out of git.

What stays outside git:

- `.env`: contains the real agent secret.
- `agent.jar`: downloaded from the controller.
- `remoting/` and `logs/`: runtime state created by the agent.

## Connect the agent

1. Create the agent definition in Jenkins first.

   In the Jenkins controller UI:

   - go to `Manage Jenkins`
   - open `Nodes`
   - click `New Node`
   - create a node, for example `local-agent`
   - choose the inbound-agent launch style
   - during agent creation in section Remote File System put e.g /home/mniedziolka/jenkins-agent/workspace

   Jenkins creates the node entry and shows a launch command containing the
   generated `-name` and `-secret` values.

2. Copy the environment template.

   ```bash 
   cp .env.example .env
   ```

3. Fill in `.env`.

   Required values:

   - `JENKINS_URL`: controller URL, for example `http://127.0.0.1:8080/`
   - `AGENT_NAME`: node name created in Jenkins, for example `local-agent`
   - `AGENT_SECRET`: secret shown in the Jenkins agent launch command

4. Download the matching remoting jar from the controller.

   ```bash 
   ./run_jenkins_agent.sh download-jar
   ```

5. Start the agent.

   ```bash 
   ./run_jenkins_agent.sh run
   ```

The agent runs in the foreground. Stop it with `Ctrl+C`.

## Useful commands

```bash
./run_jenkins_agent.sh status
./run_jenkins_agent.sh clean
./run_jenkins_agent.sh reset
```

- `status`: shows the configured controller URL and whether runtime files exist.
- `clean`: removes runtime directories but keeps `agent.jar`.
- `reset`: removes runtime directories and `agent.jar`.

## Jenkins side

Create a node in Jenkins using the inbound-agent style connection. Jenkins will
generate the launch command for that node. Copy the `-name` value into
`AGENT_NAME` and the `-secret` value into `AGENT_SECRET`, then run the local
script from this directory.