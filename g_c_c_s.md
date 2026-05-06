# Git Commands Cheat Sheet

This file collects the Git commands discussed in the thread, plus a few extra useful ones.

## What matters

- `git pull` gets the newest commits from the remote and updates your current branch.
- `git checkout` switches branches or restores one file from another branch.
- `git cherry-pick` applies one existing commit onto your current branch.
- `git revert` creates a new commit that undoes an older commit.
- `git push -u` pushes a new branch and sets its upstream tracking branch.

## Basic branch commands

Show local branches:

```bash
git branch
```

Show local and remote branches:

```bash
git branch --all
```

Refresh local knowledge of remote branches, then list them again:

```bash
git fetch --all --prune
git branch --all
```

Refresh only `origin`, then list branches again:

```bash
git fetch origin --prune
git branch --all
```

Show only remote-tracking branches:

```bash
git branch --remotes
```

Check which remote URLs Git is using:

```bash
git remote -v
```

Comments:

- `branch` lists branches.
- `--all` includes remote-tracking branches such as `origin/main`.
- `fetch` updates your local knowledge about remote branches without merging into your current branch.
- `--prune` removes remote-tracking branches that no longer exist on the server.
- `--remotes` shows only remote-tracking branches.
- `remote -v` shows the fetch and push URLs for each remote.

Switch to `main`:

```bash
git checkout main
```

If your repository still uses `master`, use:

```bash
git checkout master
```

Create and switch to a new branch:

```bash
git checkout -b jenkinsfile-only
```

Publish a newly created branch to the remote:

```bash
git push -u origin jenkinsfile-only
```

Comments:

- `checkout` switches branch or file state.
- `-b` creates the branch first, then switches to it.
- `push -u origin <branch>` publishes the local branch and sets upstream tracking.

## Update your branch

Pull the newest changes for the current branch:

```bash
git pull
```

Comments:

- `pull` is roughly `fetch + merge`.
- Use it before starting new work on top of `main` or `master`.

See what changed locally:

```bash
git status
git diff
```

Comments:

- `status` shows modified, staged, and untracked files.
- `diff` shows the actual unstaged line-by-line changes.

## Merge only one file into another branch

This is useful when you want to merge only `Jenkinsfile` and not other files from the source branch.

Start from the target branch:

```bash
git checkout master
git pull
git checkout -b jenkinsfile-only
```

Take only one file from another branch:

```bash
git checkout your-feature-branch -- j_con/Jenkinsfile
```

Review and commit it:

```bash
git status
git diff -- j_con/Jenkinsfile
git add j_con/Jenkinsfile
git commit -m "Update Jenkinsfile only"
```

Push the branch:

```bash
git push -u origin jenkinsfile-only
```

Comments:

- `branch -- file` copies one file from another branch into your current branch.
- `add` stages the selected file.
- `commit -m` creates a commit with a message.
- `push -u` sets upstream, so next time plain `git push` is enough.

## Cherry-pick one commit

Use this when the wanted change is already isolated in a single commit.

```bash
git checkout master
git pull
git checkout -b jenkinsfile-only
git cherry-pick <commit-sha>
git push -u origin jenkinsfile-only
```

Comments:

- `cherry-pick` replays one commit onto the current branch.
- `<commit-sha>` is the commit id, for example `a1b2c3d`.

Find commit ids:

```bash
git log --oneline --decorate --graph -10
```

Comments:

- `--oneline` shows short commit output.
- `--decorate` shows branch and tag labels.
- `--graph` draws a small commit tree.
- `-10` limits the output to 10 commits.

## Revert a commit safely

Use revert on shared branches when a commit already exists on remote.

```bash
git checkout master
git pull
git revert <commit-sha>
git push
```

Safer review flow through a new branch:

```bash
git checkout master
git pull
git checkout -b revert-bad-commit
git revert <commit-sha>
git push -u origin revert-bad-commit
```

Comments:

- `revert` does not delete history.
- It creates a new commit that undoes the older commit.

## Push your work

Push current branch:

```bash
git push
```

Push new branch and track remote branch:

```bash
git push -u origin my-branch
```

Comments:

- `origin` is the default remote name in most repositories.
- `-u` means `--set-upstream`.

## Restore one file from Git

Discard local changes in one file and restore it from the current branch tip:

```bash
git restore j_con/Jenkinsfile
```

Restore one file from another branch:

```bash
git checkout main -- j_con/Jenkinsfile
```

Comments:

- `restore` is clearer when you want to discard local file changes.
- `checkout branch -- file` is useful when you want a file from another branch.

## Useful inspection commands

Show last commits:

```bash
git log --oneline -5
```

Show who changed a file line by line:

```bash
git blame j_con/Jenkinsfile
```

Show differences between your branch and `main` for one file:

```bash
git diff main -- j_con/Jenkinsfile
```

Comments:

- `blame` helps answer who changed a line and in which commit.
- `diff main -- file` limits comparison to one file.

## GitHub UI note

GitHub usually merges commits or pull requests, not individual files.

If you want only one file to go to `master`, the usual flow is:

1. Create a branch from `master`.
2. Bring only that file onto the branch.
3. Commit and push it.
4. Open a pull request.

If you need to undo a merged pull request in GitHub UI, use the `Revert` button on the merged PR when GitHub offers it.

## Recommended daily mini-flow

```bash
git checkout main
git pull
git checkout -b my-task-branch
git status
git add .
git commit -m "Describe the change"
git push -u origin my-task-branch
```

Short rule:

- `status` before commit
- `diff` before add
- `push -u` on first push
- `revert` instead of history rewrite on shared branches