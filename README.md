# git merge

The `git merge` command lets you take the independent lines of development and integrate them into single branch. In this exercise, we will simulate a collaborating scenario:

1. Add and commit an empty file, called `about-git.md`.
1. Push this commit of this branch to remote site.
1. Add text "# About Git" into the `about-git.md` file.
1. Simulate user Alice:

  * set up her user name,
  * set up her email,
  * clone this repository,
  * switch to `merge-changes` branch
  * add text "Git is a distributed version control system." (without quote) into the `about-git.md` file
  * add and commit her change of this branch to remote repository

1. Back to yourself, use `git pull` command to fetch new content and merge new changes.
1. We will see the "Merge conflict" message. So we will manually merge the content, commit this new change, and push it back to your repository.
