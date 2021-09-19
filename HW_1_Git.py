(base) admin@MacBook-Pro cursor_git_hw % mkdir cursor_git
(base) admin@MacBook-Pro cursor_git_hw % cd cursor_git/
(base) admin@MacBook-Pro cursor_git % touch first.py
(base) admin@MacBook-Pro cursor_git % git add cursor.py
fatal: pathspec 'cursor.py' did not match any files
(base) admin@MacBook-Pro cursor_git % git add first.py
(base) admin@MacBook-Pro cursor_git % git commit -a -m "add first.py"
[cursor f4dfca6] add first.py
 Committer: admin <admin@MacBook-Pro.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 4 insertions(+), 1 deletion(-)
 create mode 100644 cursor_git_hw/cursor_git/first.py
(base) admin@MacBook-Pro cursor_git % touch second.py
(base) admin@MacBook-Pro cursor_git % git add second.py
(base) admin@MacBook-Pro cursor_git % git commit -a -m "add second.py"
[cursor 1408c9d] add second.py
 Committer: admin <admin@MacBook-Pro.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 cursor_git_hw/cursor_git/second.py
(base) admin@MacBook-Pro cursor_git % rm first.py
(base) admin@MacBook-Pro cursor_git % git status
warning: could not open directory '.Trash/': Operation not permitted
warning: could not open directory 'Documents/': Operation not permitted
warning: could not open directory 'Downloads/': Operation not permitted
On branch cursor
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    first.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../../.CFUserTextEncoding
        ../../.DS_Store
        ../../.IdentityService/
        ../../.anaconda/
        ../../.android/
        ../../.anydesk/
        ../../.condarc
        ../../.config/
        ../../.idlerc/
        ../../.ipython/
        ../../.jupyter/
        ../../.mono/
        ../../.python_history
        ../../.ssh/
        ../../.templateengine/
        ../../.viminfo
        ../../.zsh_history
        ../../.zsh_sessions/
        ../../.zshrc
        ../../10
        ../../Applications/
        ../../Creative Cloud Files/
        ../../Demo/
        ../../Desktop/
        ../../Homeworks/
        ../../Library/
        ../../Movies/
        ../../Music/
        ../../Pictures/
        ../../Public/
        ../../PycharmProjects/.DS_Store
        ../../PycharmProjects/pythonProject/#3.py
        ../../PycharmProjects/pythonProject/.DS_Store
        ../../PycharmProjects/pythonProject/.idea/
        ../../PycharmProjects/pythonProject/HW# 10 calculator.py
        ../../PycharmProjects/pythonProject/Py_10_robot.py
        ../../PycharmProjects/pythonProject/cursor_git.hw/
        ../../PycharmProjects/pythonProject/files_contextmanagers_hw.zip
        ../../PycharmProjects/pythonProject/lesson 9.py
        ../../PycharmProjects/pythonProject/main.py
        ../../PycharmProjects/pythonProject/task1backup.txt
        ../../PycharmProjects/pythonProject/test
        ../../PycharmProjects/pythonProject/venv/
        ../../cursor/
        ../.DS_Store
        ../.idea/
        ../HW_14.py
        ../homework.sh
        ../hw1.sh
        ../hw1.txt
        ../hw2.sh
        ../hw3.sh
        ../linux_lecture/
        ../linuxs_lecture
        ../ls_notes.sh
        ../main.py
        ../notes.sh
        ../../file.txt
        "../../file.txt\320\220 "
        ../../first.first.txt
        ../../hashed_feature.csv
        ../../opt/
        ../../progam.py
        ../../program.py
        ../../tabular_data.csv
        ../../test.csv
        ../../train.csv
        ../../txt.maliarchuk

no changes added to commit (use "git add" and/or "git commit -a")
(base) admin@MacBook-Pro cursor_git % git push
fatal: The current branch cursor has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin cursor

(base) admin@MacBook-Pro cursor_git % git branch first
(base) admin@MacBook-Pro cursor_git % git branch second
(base) admin@MacBook-Pro cursor_git % git checkout -b second
fatal: A branch named 'second' already exists.
(base) admin@MacBook-Pro cursor_git % echo "pint"Hello"" > second.py
(base) admin@MacBook-Pro cursor_git % git add second.py
(base) admin@MacBook-Pro cursor_git % git commit -a -m "changing second.py"
[cursor fb61afc] changing second.py
 Committer: admin <admin@MacBook-Pro.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 1 insertion(+)
 delete mode 100644 cursor_git_hw/cursor_git/first.py
(base) admin@MacBook-Pro cursor_git % git chckout first
git: 'chckout' is not a git command. See 'git --help'.

The most similar command is
        checkout
(base) admin@MacBook-Pro cursor_git % git checkout first
Switched to branch 'first'
(base) admin@MacBook-Pro cursor_git % git checkout master
error: pathspec 'master' did not match any file(s) known to git
(base) admin@MacBook-Pro cursor_git % git merge first
Already up to date.
(base) admin@MacBook-Pro cursor_git % git merge second
Already up to date.
(base) admin@MacBook-Pro cursor_git % echo "print('Cursor')" > second.py
(base) admin@MacBook-Pro cursor_git % git add second.py
(base) admin@MacBook-Pro cursor_git % git commit -a -m "Changing second.py"
[first a6d0b42] Changing second.py
 Committer: admin <admin@MacBook-Pro.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
(base) admin@MacBook-Pro cursor_git % git push
fatal: The current branch first has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin first

(base) admin@MacBook-Pro cursor_git % git merge first
Already up to date.
(base) admin@MacBook-Pro cursor_git % git merge second
Already up to date.
(base) admin@MacBook-Pro cursor_git %
