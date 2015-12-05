# Rewriting history

## git commit --amend

The `git commit --amend` command lets you combine staged changes with the previous commit instead of committing it as a new snapshot, or simply edit previous commit message without changing its snapshot. In this exercise, do the following:

```
# Add a new file
touch new-file.txt
git add new-file.txt
git commit -m "Add new-file.txt file"

# Add another new file
touch another-new-file.txt
git add another-new-file.txt
# Combine staged changes
git commit --amend

# Edit previous commit message
git commit --amend
```

## git rebase

The `git rebase` command lets you move your current branch to a new base commit (e.g. hash ID, branch name, tag name, or relative reference to HEAD). In this exercise, use `git rebase -i` to combine 4 commits of "Add ... line of the poem" into 1 commit.
