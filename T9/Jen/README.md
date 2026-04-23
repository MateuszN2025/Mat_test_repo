# Jenkins Docker Setup

This setup gives you a reproducible local Jenkins instance with:

- a custom Jenkins image
- preinstalled plugins for pipeline and test reporting
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
./manage.sh up
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
./manage.sh down
./manage.sh up
```

## View logs

```bash
./manage.sh logs
```

## Reset Jenkins completely

This removes all jobs, users, and history stored in the named volume.

```bash
./manage.sh reset
```

## Recommended next step

After Jenkins starts, create a Pipeline job and point it at your automation repository. A minimal `Jenkinsfile` should:

- create a virtual environment
- install Python dependencies
- run `pytest`
- publish `JUnit` XML reports

## Notes

- `JENKINS_URL` should match the URL you actually open in the browser.
- If port `8080` is already in use, change `JENKINS_HTTP_PORT` in `.env`.
- If you already have a manually started Jenkins container on `8080`, stop or remove it before using `./manage.sh up`.
- If you later expose Jenkins over a real network, add HTTPS and stronger access control.
- This configuration is intentionally unsecured and should stay local-only.
- `compose.yaml` is still included for Docker Compose users, but this environment does not currently have a working compose subcommand.