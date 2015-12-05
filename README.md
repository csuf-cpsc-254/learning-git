# git checkout, git revert , git reset, and git clean

The `git checkout` command serves three distinct functions: checking out files, checking out commits, and checking out branches. Checking out a file from a commit or a branch make a copy of the file or overwrite that file in the working directory, while checking out a commit or a branch makes the entire working directory match that commit or that branch.

The `git revert` command undoes a committed snapshot by figuring out how to undo the changes introduced by the previous commit and append a NEW commit with the resulting content.

The `git reset` command undoes a committed snapshot and the following commits will be permanently removed.

The `git clean` command removes untracked files from your working directory.

In this exercise, we will do your own exploration of each command.
