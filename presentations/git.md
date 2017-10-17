# Version Control with git

## What is Version Control
- A way to track changes
- A way to collaboratively develop
- A way to maintain a project's history
- A way to safely experiment on a repository

## What is git?
- The most popular of a suite of VCS tools that have existed over the years
- Good enough for the kernel
- Easily integrated with the online service GitHub to remotely host a repository,
  track bugs, manage code reviews, etc.
- Not just for code! Avoid binary blobs and things that don't diff well, but
  tracking text files, TeX files, etc. are all encouraged! Version controlling
  your thesis, dissertation, or manuscript will save you hours of heartache.

## Getting started
- git is available on all modern platforms
- Linux: available from package manager
- macOS: xcode-select --install
- Windows: GitHub Desktop (http://desktop.github.com)
- Check your installation: `git --version`

## Setting up Git
- We need to setup our name, email, and preferences in git. These can be set
  on a repository by repository basis or globally. Here we'll set them globally.
  Your commits will contain this contact information.
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
- What is a repository? A place where tracked documents live and that contains
  the history of these documents as a series of diffs.
- Let's make a simple project to experiment with.
- `mkdir project_code`
- `cd project_code`
- While we're here, let's create a simple file that contains some code. Using
  your favorite editor, create `calc.py` with the following function:
  ```python
  def wind_speed(u, v):
     """Calculates wind speed from u and v components."""
     return sqrt(u * u + v * v)
  ```
- Now that we've got a project going, let's setup a git repository. Doing this
  is straight forward and you should do it even on "toy" projects.
- `git init`
- Note `.git` directory created that contains all Git information in repository
- We can also see the state of the repository and the current files with
  `git status`

## Adding files
- Now we've got a file in the repository and the `git status` command shows us
  that we have an untracked file. Let's start tracking it. Before that we need
  to understand the stages of making a commit to a git repository.

### Making a commit
- Unstaged Changes: Things that are different in your project than from the
  committed materials in the repository. These are not ready to be committed
  yet.
- Staged Changes: Things that are different, but are ready to be committed.
- Committed Changes: Changes committed to the repository.

- Let's add our `calc.py` file to the files that git knows about and is tracking.
  You'll want to track your source files, but other files like compiled binaries,
  TeX aux files, etc. you don't need to track.
- `git add calc.py`
- Now when we run `git status`, we'll see that the file is staged to be committed.
- You use the `git add` command to stage existing tracked files as well as start
  tracking new files.

## Tracking Changes
- As happens in all projects, we need to make a change. I wrote that for u and
  v components only. Silly me - there are sonic anemometers now that have w
  component readings as well!
- edit `calc.py`
  ```python
  def wind_speed(u, v, w):
     """Calculates wind speed from u and v components."""
     return sqrt(u * u + v * v + w * w)
  ```
- Note that the file is now tracked and changed, but not staged `git status`
- Stage it: `git add calc.py`
- `git status`
- Make a commit: `git commit -m "Add calculations file"`
- Now everything is up to date!: `git status`
- Now we'll look at some more commands to help us see what we've changed
- We did a silly thing, we require w component data. That's not always around! Let's
  provide a default of zero.
  - edit `calc.py`
    ```python
    def wind_speed(u, v, w=0):
       """Calculates wind speed from u and v components."""
       return sqrt(u * u + v * v + w * w)
    ```
- See the file with unstaged changes: `git status`
- Lets see line-by-line changes: `git diff`
- Stage the file: `git add calc.py`
- Now there's nothing in the diff: `git diff`
- To see the diff with staged files: `git diff --staged`
- Make the new commit: `git commit -m "Make w an optional parameter with a zero default."`
- We are back to a clean working directory: `git status`

### Exercise
- Create a new file called `process_data.py` with the following content:
  ```python
  from calc import wind_speed

  print(wind_speed(1, 2, 3))
  ```
  - Start tracking this file with git and commit it to the repository.

## History
- One of the perks of version control is being able to track the history of the
  files in the repository. Here we'll go back through our repository's short
  history.
- Scroll through the history: `git log`
- Just see the last entry in the log: `git log -1`
- More condensed just showing the commmit message: `git log --oneline`
- Show the change stats in each commit: `git log --stat`
- Show diff for a particular commit: `git diff [longhashhere]`
- But you don't have to use the full hash: `git diff [shorthashhere]`
- View a specific commit's log message and diff: `git show [shorthashhere]`
- Make some changes to our file `calc.py`
  ```python
  def wind_speed(u, v, w=np.zeros_like(u)):
     """Calculates wind speed from u and v components."""
     return sqrt(u * u + v * v + w * w)
  ```
- We can eliminate those changes by checking out the last committed version
  of our file: `git checkout HEAD calc.py`
- We can also checkout a specific version: `git checkout [hash] calc.py`
- That file now shows up as modified and could be committed: `git status`
- Checkout the last committed version of the file: `git checkout -- calc.py`

## Ignoring Things
- There are often certain files or types of files that we do not want to include
  in our repository. These include compiled binaries, raw data files (sometimes),
  intermediate analysis products, etc. Let's create some fake data files and then
  exclude them from our repository.
- Create a new directory: `mkdir results`
- Make the fake data files: `touch a.dat b.dat c.dat results/a.out results/b.out`
- They show up as new and untracked. That could get annoying: `git status`
- We can add these files or file types to the `.gitignore` file and git will
  pretend like they are not there.
  ```
  a.dat
  b.dat
  *.out
  ```
- Gone!: `git status`
- But now we will need/want to track our git ignore file so other contributors
  won't commit data files or so we won't on another machine: `git add .gitignore`
- Commit the git ignore file: `git commit -m "Add ignore file."`
- Make sure we're clean again: `git status`
- Let's add another file: `git add a.out`
- We can still see what we are ignoring: `git status --ignored`

## Branching and Merging
- Let's say we want to try adding a new feature. We want to do this in a little
  separate experimental space. In the old days you probably copied the folder
  with your code and named it `mycode_works_oct12_1_2_a` or something similar.
  Instead, we can just create a branch with git!
- Create a new branch: `git branch unit_conversion`
- We're still on master: `git status`
- List the branches in existance: `git branch`
- Checkout our new branch: `git checkout unit_conversion`
- Check the status: `git status`
- See where we are in the branch list: `git branch`
- edit `calc.py`
  ```python
  def wind_speed(u, v, w=np.zeros_like(u)):
     """Calculates wind speed from u and v components."""
     return sqrt(u * u + v * v + w * w)


  def knots_to_mph(speed):
    return speed * 1.15078
  ```
- Stage the file: `git add calc.py`
- Commit the file: `git commit -m "Add knots to mph conversion."`
- Look at the log and see the commit: `git log`
- Go back to the master branch: `git checkout master`
- The commit isn't there yet! It's just on the branch: `git log`
- Let's merge our feature branch onto master: `git merge unit_conversion`
- Our commit is there now!: `git log`
- Now we can delete our feature branch as it's been merged: `git branch -d unit_conversion`
- You can combine creating a branch and checking it out with this
  shorthand: `git checkout -b my-new-branch`

### Exercise
- Create a new branch that adds a conversion from mph to knots.
- Implement the feature
- Merge it back to master
- Delete the branch

## Grabbing a Remote Repository
- Let's go back out of this repository's directory and to where ever we want
  to put our new clong of a remote repository: `cd ..`
- Using the clone command we can get a copy of the remote repository (and all
  of its history) on our machine: `git clone https://github.com/Unidata/unidata-python-workshop`
- Look at what we got: `cd unidata-python-workshop`

## Resources
- [Illustrated git Cheatsheet](http://illustrated-git.readthedocs.org)
- [Pro Git](https://git-scm.com/book/en/v2)
