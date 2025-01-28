# Git Overview

Git is a powerful, distributed version control system that allows developers to track changes in their code, collaborate with others, and manage multiple versions of a project. 

## Key Features
- **Distributed Version Control**: Git allows multiple developers to work on the same project without overwriting each other’s changes.
- **Branching and Merging**: Git’s branching model allows developers to create separate branches for new features, bug fixes, or experiments and later merge them back into the main branch.
- **Collaboration**: Developers can clone repositories, make changes, and push updates to a central repository.
- **Staging Area**: Git allows changes to be staged before they are committed, making it easier to organize updates.
- **History and Revert**: Git keeps a complete history of all changes, allowing developers to track changes, revert to previous versions, and analyze project history.



## Git terminal commands

| **Command**                     | **Description**                                                   |
|----------------------------------|-------------------------------------------------------------------|
| `git init`                       | Initialize a new Git repository.                                  |
| `git clone <url>`                | Clone an existing repository from a URL.                          |
| `git status`                     | Check the current status of the repository (staged, untracked, etc.).|
| `git add <file-name>`            | Stage a file for commit.                                          |
| `git add .`                       | Stage all modified files for commit.                              |
| `git commit -m "message"`        | Commit staged changes with a message.                             |
| `git log`                        | View the commit history.                                          |
| `git branch`                     | List all branches in the repository.                              |
| `git branch <branch-name>`       | Create a new branch.                                              |
| `git checkout <branch-name>`     | Switch to a different branch.                                     |
| `git merge <branch-name>`        | Merge changes from the specified branch into the current branch.  |
| `git push origin <branch-name>`  | Push commits to a remote repository on the specified branch.      |
| `git pull`                       | Fetch and merge changes from the remote repository.               |
| `git remote -v`                  | Show remote repository URLs.                                      |
| `git fetch`                      | Fetch changes from the remote repository without merging them.    |
| `git diff`                       | Show changes that have been made but not yet staged for commit.   |
| `git reset`                      | Unstage a file or reset changes.                                  |
| `git reset --hard`               | Reset the repository to a previous commit (erases changes).       |
| `git stash`                      | Temporarily store uncommitted changes.                            |
| `git stash pop`                  | Apply stashed changes back into the working directory.            |
| `git tag <tag-name>`             | Create a new tag at the current commit.                           |

## Git Staging and Committing Process

The following link is a diagram illustrating the flow of staging and committing in Git:

!File Status Lifecycle(https://i.stack.imgur.com/ppgRW.png)

# Git Hub Overview

GitHub is a cloud-based platform that hosts Git repositories. It allows developers to share and collaborate on code with other developers from around the world.

## How to Create a GitHub Account

Follow these steps to create your GitHub account:

---

## **1. Visit GitHub's Website**
   - Open your browser and go to [GitHub's website](https://github.com).

## **2. Click on "Sign Up"**
   - On the GitHub homepage, click the **Sign Up** button in the top-right corner.

## **3. Enter Your Details**
   - **Email Address**: Provide a valid email address.
   - **Password**: Create a strong password (a mix of letters, numbers, and special characters is recommended).
   - **Username**: Choose a unique username. This will be your GitHub handle (e.g., `https://github.com/yourusername`).
   

## **4. Verify Your Account**
   - Complete the CAPTCHA challenge to prove you're not a robot.

## **5. Email Verification**
   - Check your email inbox for a verification email from GitHub.
   - Click the link in the email to verify your account.

## **6. Start Exploring GitHub**
   - Create your first repository or explore public repositories on GitHub.

---

## **Tips for Setting Up Your GitHub Account**
- Use a professional or recognizable username if you'll use GitHub for work or public projects.
- Enable **two-factor authentication (2FA)** for added security.
- Add a personal access token to use GitHub from the command line or integrate with other tools.

---

## **Getting Started on GitHub**
Once your account is set up:
1. **Create a Repository**: 
   - A repository is where your project files are stored.
2. **Install Git**:
   - To use Git on your local machine, [download Git](https://git-scm.com/) and install it.
3. **Learn Git Commands**:
   - Practice basic commands like `git clone`, `git add`, `git commit`, and `git push`.

---


### Key Features of GitHub:
- **Remote Repositories**: Store your Git repositories in the cloud for easy access and collaboration.
- **Pull Requests**: Propose changes to a project by creating a pull request, which can be reviewed, discussed, and merged into the main project.
- **Collaboration**: Work on projects with others, track issues, and provide feedback in discussions.
- **Integration with CI/CD**: Easily integrate with continuous integration and continuous delivery tools to automate your development pipeline.
- **GitHub Actions**: Automate workflows for testing, building, and deploying applications.

# GitHub Commands Table

| **Command**                                  | **Description**                                                                                   |
|----------------------------------------------|---------------------------------------------------------------------------------------------------|
| `git clone <repository-url>`                 | Clone a GitHub repository to your local machine.                                                 |
| `git remote add origin <repository-url>`     | Add a remote repository (GitHub) to your local Git repository.                                   |
| `git push origin <branch-name>`              | Push commits from your local repository to a GitHub repository on the specified branch.          |
| `git pull origin <branch-name>`              | Fetch and merge changes from a GitHub repository to your local branch.                          |
| `git fetch origin`                           | Fetch changes from a GitHub repository without merging them.                                     |
| `git branch -r`                              | List all remote branches in a GitHub repository.                                                 |