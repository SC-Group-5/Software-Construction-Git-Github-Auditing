## Using Git

### First Steps with Git
Before using Git, basic configuration is required so Git can track who made each change. This is done using the `git config` command to set a username and email. These details are stored and attached to every commit.

To start working with Git, there are two main options:
- **Initialize a new repository** using `git init`
- **Copy an existing repository** using `git clone`

When `git init` is run, Git creates a hidden **Git directory (`.git`)**. This directory acts as a database that stores the project’s history and snapshots. Everything outside this directory is called the **working tree**, which contains the current version of the project files.


### Git Project Structure
A Git project is made up of three main parts:
- **Git directory** – stores the complete history of changes
- **Working tree** – where files are created and modified
- **Staging area** – holds changes prepared for the next commit

Git records changes by taking **snapshots**. Each snapshot represents the exact state of the project at a specific point in time. These snapshots together form the project’s history.


### Tracking Files in Git
Files in Git can be either **tracked** or **untracked**.
- **Untracked files** are new files not yet added to Git
- **Tracked files** are files Git monitors for changes

Tracked files move through three main states:

1. **Modified** – the file has been changed but not staged
2. **Staged** – the file is marked to be included in the next commit
3. **Committed** – the changes are saved permanently in the Git directory

The typical workflow is:
- Edit files in the working tree
- Stage changes using `git add`
- Save changes using `git commit`

The `git status` command is used to check the current state of files at any point.


### Making Commits
A **commit** saves staged changes as a snapshot in the Git directory. Commits should always include a **commit message**, which explains what was changed and why.
Commits can be created by:
- Running `git commit` (opens a text editor)
- Running `git commit -m "message"` (adds message directly)

Each commit stores:
- A unique commit ID
- Author name and email
- Date and time
- Commit message


### Anatomy of a Commit Message
A good commit message improves collaboration and future understanding.
A well-structured commit message includes:
- **Short summary line** (about 50 characters)
- **Blank line**
- **Detailed description** (lines under 72 characters)

Commit messages should explain **why** the change was made, not just **what** was changed. Avoid vague messages like *“fix”* or *“update”*.

The `git log` command is used to view commit history in a readable format.


### Key Terms and Definitions

- **Version Control System (VCS):** A tool that tracks code changes, supports collaboration, and stores history
- **Git:** A free, open-source version control system
- **Repository:** A storage location for a project and its history
- **Git directory:** Explained earlier; stores snapshots and history
- **Working tree:** Current project files
- **Staging area:** Holds changes for the next commit
- **Tracked files:** Files Git monitors
- **Untracked files:** Files Git does not yet monitor
- **Modified files:** Files changed but not staged
- **Staged files:** Files ready to be committed
- **Commit:** A saved snapshot of changes
- **Commit message:** Description of a commit
- **Git log:** Displays commit history
- **Diff:** Shows differences between files
- **Patch:** Applies detected changes to files
- **SCM:** Source Control Management, similar to VCS


### Summary
Git helps manage project history by tracking file changes through a structured workflow. By modifying, staging, and committing files, developers can safely record progress, collaborate effectively, and understand how a project evolves over time.
