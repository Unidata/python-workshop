# Version Control with git

## What is Version Control

## What is git?

## Getting started

- git is available on all modern platforms
- Linux: available from package manager
- macOS: xcode-select --install
- Windows: GitHub Desktop (http://desktop.github.com)
- `git --version`

## Setting up Git
- `git config --global --add user.email me@me.com`
- `git config --global --add user.name "My Name"`
- `git config --global --add color.ui auto`
- `git config --list`

## How Git Works
Draw diagram on the board showing:
- commits
- head
- rollback
- branch/merge

## Creating a Git Repository
- What is a repository?
- `mkdir project_code`
- `cd project_code`
- `git init`
- Note `.git` directory that contains all Git information in repository
- `git status`

## Tracking Changes
- edit `calc.py`
- Commits
- `git add calc.py`
- `git status`
- `git commit -m "Add calculations file"`
- `git status`
- edit `calc.py`
- `git status`
- `git diff`
- `git add calc.py`
- `git diff`
- `git diff --staged`
- `git commit -m "Add new calcuation"`
- `git status`

### Exercise: Add a new file to git.

## History
- `git log`
- `git log -1`
- `git log --oneline`
- `git log --stat`
- `git diff [longhashhere]`
- `git diff [shorthashhere]`
- `git show [shorthashhere]`
- edit `calc.py`
- `git checkout HEAD calc.py`
- `git checkout [hash] calc.py`
- `git status`
- `git checkout -- calc.py`

## Ignoring Things
- `mkdir results`
- `touch a.dat b.dat c.dat results/a.out results/b.out`
- `git status`
- edit `.gitignore`
- `git status`
- `git add .gitignore`
- `git commit -m "Add ignore file."`
- `git status`
- `git add a.out`
- `git status --ignored`

## Branching and Merging
- `git branch test-kelvin`
- `git status`
- `git branch`
- `git checkout test-kelvin`
- `git status`
- `git branch`
- edit `calc.py`
- `git add calc.py`
- `git commit -m "Add Kelvin calculation"`
- `git log`
- `git checkout master`
- `git log`
- `git merge test-kelvin`
- `git log`
- `git branch -d test-kelvin`
- shorthand: `git checkout -b my-new-branch`

### Exercise: Go do some development on a branch and merge back

## Grabbing a Remote Repository
- `cd ..`
- `git clone https://github.com/Unidata/unidata-python-workshop`
- `cd unidata-python-workshop`

http://illustrated-git.readthedocs.org
