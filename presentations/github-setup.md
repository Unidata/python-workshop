# Github instructions for experimentation with dummy repo

## Sign up

If you do not have one already, [sign up for a github account](https://github.com/join). Please remember your login and password when attending workshop.

### github setup

- Login to github.

- Fork the workshop repository: <https://github.com/Unidata/dummy> by clicking the fork button.

![Fork](https://github-images.s3.amazonaws.com/help/repository/fork_button.jpg)


```
git config --global user.name "YOUR NAME"

git config --global user.email "YOUR EMAIL ADDRESS"

git clone https://github.com/YOUR-USERNAME/dummy

cd dummy

git remote add upstream https://github.com/unidata/dummy.git

git fetch upstream

#sanity check, should see 'origin' and 'upstream' remotes
git branch -a

# Later if you wish to save (i.e., push out) your commits
git push origin master

```
