# Standard New Commit
1. Go to github page => Create a new issue in xiaoxianma/xiaomanager
2. git checkout -b <project/feature> if not exists
3. git rebase master & git push to keep update to date
4. development
5. commit message following commit template
6. "git push -u origin <project/feature>" or "git push" for short
7. Go to github page => "New pull request" under Pull requests section => master <- <project/feature> => Create pull request
8. Go to github page => Review and Merge pull request

# Amend commit
1. development  
2. git commit --amend --no-edit
3. git push --force

# Multiple commits
1. add more commits
2. Do PR

# Setup git commit template
1. copy development_guide/.gitmessage to your home directory
2. git config --global commit.template ~/.gitmessage

