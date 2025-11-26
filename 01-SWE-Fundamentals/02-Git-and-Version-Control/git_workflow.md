# Git Workflow Guide

This guide covers the basic workflow for working with Git in a collaborative environment.

## 1. Pull Latest Changes

Before starting any new work, always sync with the remote repository:

```bash
# Switch to main branch
git switch main

# Pull latest changes from remote
git pull origin main
```

## 2. Create a New Branch

Create a feature branch for your work:

```bash
# Create and switch to a new branch
git switch -c feature/your-feature-name

# Alternative: create branch and switch separately
git branch feature/your-feature-name
git switch feature/your-feature-name
```

**Branch naming conventions:**
- `feature/description` - for new features
- `bugfix/description` - for bug fixes
- `hotfix/description` - for urgent fixes
- `docs/description` - for documentation updates

## 3. Make Changes

Work on your code, add files, modify existing files, etc.

```bash
# Check status of your changes
git status

# See what changes you've made
git diff
```

## 4. Stage and Commit Changes

Stage your changes and create commits:

```bash
# Stage specific files
git add file1.py file2.js

# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Add user authentication feature"
```

**Commit message best practices:**
- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Be descriptive but concise
- Reference issue numbers if applicable

## 5. Push to Remote

Push your branch to the remote repository:

```bash
# First time pushing a new branch
git push -u origin feature/your-feature-name

# Subsequent pushes
git push
```

## 6. Create a Pull Request

1. Navigate to your repository on GitHub/GitLab/etc.
2. Click "New Pull Request" or "Create Merge Request"
3. Select your feature branch as source and main as target
4. Fill in:
   - **Title**: Clear, descriptive summary
   - **Description**: What changes were made and why
   - **Reviewers**: Team members who should review
   - **Labels**: Appropriate tags (feature, bugfix, etc.)

## 7. Code Review Process

1. **Address feedback**: Make changes based on reviewer comments
2. **Update your branch**: Add commits to address review feedback
3. **Push updates**: `git push` to update the pull request

```bash
# If you need to update after review
git add .
git commit -m "Address review feedback: fix validation logic"
git push
```

## 8. Merge the Pull Request

Once approved:

1. **Squash and merge** (recommended for clean history)
2. **Create merge commit** (preserves branch history)
3. **Rebase and merge** (cleanest linear history)

## 9. Clean Up

After merging, clean up your local environment:

```bash
# Switch back to main
git switch main

# Pull the latest changes (including your merged code)
git pull origin main

# Delete the local feature branch
git branch -d feature/your-feature-name

# Delete the remote branch (if not auto-deleted)
git push origin --delete feature/your-feature-name
```

## Common Commands Cheat Sheet

```bash
# Check current status
git status

# See commit history
git log --oneline

# Switch branches
git switch branch-name

# Create new branch from current location
git switch -c new-branch-name

# See all branches
git branch -a

# Stash uncommitted changes
git stash
git stash pop

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo changes to a file
git checkout -- filename
```

## Best Practices

1. **Keep commits atomic** - each commit should represent one logical change
2. **Write clear commit messages** - future you will thank you
3. **Pull before pushing** - avoid unnecessary merge conflicts
4. **Use descriptive branch names** - make it clear what the branch is for
5. **Review your own changes** - check your diff before committing
6. **Don't commit directly to main** - always use feature branches
7. **Keep branches short-lived** - merge frequently to avoid large conflicts

## Handling Merge Conflicts

When conflicts occur during merge/rebase:

```bash
# See which files have conflicts
git status

# Edit files to resolve conflicts (look for <<<<<<< markers)
# After resolving conflicts:
git add resolved-file.py
git commit

# For rebase conflicts:
git rebase --continue
```

## Emergency Commands

```bash
# Undo last commit completely
git reset --hard HEAD~1

# Revert a commit (creates new commit that undoes changes)
git revert commit-hash

# Force push (use with caution!)
git push --force-with-lease
```

**⚠️ Warning**: Use `--force` commands carefully, especially on shared branches!
