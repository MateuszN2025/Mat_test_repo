# Jenkins Agent Backup

This directory stores the files needed to recreate a local Jenkins inbound agent without committing the live runtime directory from `/home/mniedziolka/jenkins-agent`.

What is versioned here:

- `jenkins_agent_creation.sh`: downloads `agent.jar` and runs the agent.
- `.env.example`: template for controller URL and agent credentials.
- `.gitignore`: keeps runtime files and secrets out of git.

What stays outside git:

- `.env`: contains the real agent secret.
- `agent.jar`: downloaded from the controller.
- `remoting/` and `logs/`: runtime state created by the agent.

## Recreate the agent

1. Copy the environment template.

   ```bash
   cp .env.example .env
   ```

2. Fill in `.env`.

   Required values:

   - `JENKINS_URL`: controller URL, for example `http://127.0.0.1:8080/`
   - `AGENT_NAME`: node name created in Jenkins
   - `AGENT_SECRET`: secret from the node page in Jenkins

3. Download the matching remoting jar from the controller.

   ```bash
   ./jenkins_agent_creation.sh download-jar
   ```

4. Start the agent.

   ```bash
   ./jenkins_agent_creation.sh run
   ```

The agent runs in the foreground. Stop it with `Ctrl+C`.

## Useful commands

```bash
./jenkins_agent_creation.sh status
./jenkins_agent_creation.sh clean
./jenkins_agent_creation.sh reset
```

- `status`: shows the configured controller URL and whether runtime files exist.
- `clean`: removes runtime directories but keeps `agent.jar`.
- `reset`: removes runtime directories and `agent.jar`.

## Jenkins side

Create a node in Jenkins using the inbound-agent style connection. Then copy the generated agent name and secret into `.env`.