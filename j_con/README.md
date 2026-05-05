# Jenkins Docker Setup

This setup gives you a reproducible local Jenkins instance with:

- a custom Jenkins image
- preinstalled plugins for pipeline and test reporting
- Allure report support through the Jenkins Allure plugin
- Configuration as Code instead of the first-run wizard
- an unsecured local-only setup so the UI opens without a login page
- a named volume for persistent Jenkins state

## Why this setup

This is a better baseline than `docker run ... jenkins/jenkins:lts` because:

- there is no login flow to get in the way of local test runs
- plugins are pinned in one visible file
- Jenkins startup is repeatable
- resetting the instance is simple and explicit

## Files

- `compose.yaml` starts Jenkins
- `Dockerfile` builds the Jenkins image with plugins and JCasC
- `plugins.txt` defines installed plugins
- `casc/jenkins.yaml` defines Jenkins configuration
- `init.groovy.d/01-admin-user.groovy` runs from Jenkins home and keeps the admin account synced with `.env`
- `.env.example` shows the required environment variables

## First start

1. Copy the environment file:

```bash
cp .env.example .env
```

2. Edit `.env` if you need to change ports or the advertised Jenkins URL.

3. Start Jenkins.

Default path on this machine:

```bash
./run_local_jenkins.sh up
```

Alternative if you have a working Compose implementation:

```bash
podman compose up -d --build
```

If you use Docker instead of Podman:

```bash
docker compose up -d --build
```

4. Open Jenkins in the browser:

```text
http://127.0.0.1:8080
```

5. Jenkins opens directly without a login screen.

There is no unlock wizard because Configuration as Code disables it.

## Stop and start

```bash
./run_local_jenkins.sh down
./run_local_jenkins.sh up
```

## View logs

```bash
./run_local_jenkins.sh logs
```

## Reset Jenkins completely

This removes all jobs, users, and history stored in the named volume.

```bash
./run_local_jenkins.sh reset
```

## Recommended next step

After Jenkins starts, create a Pipeline job and point it at your automation repository. A minimal `Jenkinsfile` should:

- create a virtual environment
- install Python dependencies
- run `pytest`
- publish `JUnit` XML reports
- publish `Allure` results

This repository now includes an example pipeline in `j_con/Jenkinsfile` with a build parameter named `TEST`.

In Jenkins:

1. Create a Pipeline job.
2. Point it at this repository and use script path `j_con/Jenkinsfile`.
3. Run `Build with Parameters`.
4. Fill `TEST` only when you want to limit what `pytest` runs.

Examples for `TEST`:

- `T11/tests`
- `T11/tests/test_example.py`
- `-k smoke`
- `-k api and not slow`

The pipeline exports the `TEST` build parameter as an environment variable and prepends it to the `pytest` command.

## Enable Allure reports

The custom Jenkins image now installs the `allure-jenkins-plugin`, so Jenkins
can publish Allure reports. One controller-side step is still required after the
first restart: configure the Allure commandline tool in the Jenkins UI.

1. Rebuild and restart Jenkins so the plugin is installed:

```bash
./run_local_jenkins.sh down
./run_local_jenkins.sh up
```

2. In Jenkins, go to `Manage Jenkins` -> `Tools`.

3. Find the `Allure Commandline` section and add one installation.

4. Keep `Install automatically` enabled and choose the latest Allure 2 version.

5. Save the tool configuration.

After that, pipeline jobs can publish Allure results with a step like:

```groovy
post {
	always {
		allure(
			includeProperties: false,
			results: [[path: 'allure-results']]
		)
	}
}
```

Python tests also need to generate Allure result files, for example by running:

```bash
pytest --alluredir=allure-results
```

## Notes

- `JENKINS_URL` should match the URL you actually open in the browser.
- If port `8080` is already in use, change `JENKINS_HTTP_PORT` in `.env`.
- If you already have a manually started Jenkins container on `8080`, stop or remove it before using `./run_local_jenkins.sh up`.
- If you later expose Jenkins over a real network, add HTTPS and stronger access control.
- This configuration is intentionally unsecured and should stay local-only.
- `compose.yaml` is still included for Docker Compose users, but this environment does not currently have a working compose subcommand.