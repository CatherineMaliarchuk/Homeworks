(base) admin@MacBook-Pro cursor_git_hw % mkdir linux_lecture
mkdir: linux_lecture: File exists
(base) admin@MacBook-Pro cursor_git_hw % touch notes.txt
(base) admin@MacBook-Pro cursor_git_hw % cp notes.txt linux_lecture
(base) admin@MacBook-Pro cursor_git_hw % ls-l
zsh: command not found: ls-l
(base) admin@MacBook-Pro cursor_git_hw % ls -l
total 24
-rw-r--r--  1 admin  staff  1049 Aug 12 22:44 HW_14.py
drwxr-xr-x  8 admin  staff   256 Sep 16 23:43 linux_lecture
-rw-r--r--  1 admin  staff    21 Sep 18 14:54 linuxs_lecture
-rw-r--r--  1 admin  staff   519 Aug 12 10:01 main.py
-rw-r--r--  1 admin  staff     0 Sep 18 15:14 notes.txt
(base) admin@MacBook-Pro cursor_git_hw % ls sort-r
ls: sort-r: No such file or directory
(base) admin@MacBook-Pro cursor_git_hw % ls -la -r
total 40
-rw-r--r--   1 admin  staff     0 Sep 18 15:14 notes.txt
-rw-r--r--   1 admin  staff   519 Aug 12 10:01 main.py
-rw-r--r--   1 admin  staff    21 Sep 18 14:54 linuxs_lecture
drwxr-xr-x   8 admin  staff   256 Sep 16 23:43 linux_lecture
-rw-r--r--   1 admin  staff  1049 Aug 12 22:44 HW_14.py
drwxr-xr-x  14 admin  staff   448 Sep 18 15:18 .idea
-rw-r--r--@  1 admin  staff  6148 Aug 14 15:39 .DS_Store
drwxr-xr-x+ 56 admin  staff  1792 Sep 18 15:14 ..
drwxr-xr-x   9 admin  staff   288 Sep 18 14:54 .
(base) admin@MacBook-Pro cursor_git_hw % mv note.txt new.notes.txt
mv: rename note.txt to new.notes.txt: No such file or directory
(base) admin@MacBook-Pro cursor_git_hw % mv notes.txt new.notes.txt
(base) admin@MacBook-Pro cursor_git_hw % rm notes.txt new.notes.txt
rm: notes.txt: No such file or directory
(base) admin@MacBook-Pro cursor_git_hw % rm new.notes.txt
rm: new.notes.txt: No such file or directory
(base) admin@MacBook-Pro cursor_git_hw % find linux_lecture
linux_lecture
linux_lecture/hw1.sh,
linux_lecture/lecture_new
linux_lecture/lecture_new/notes.txt
linux_lecture/lecture_new/hw1.txt
linux_lecture/lecture_new/homework.sh
linux_lecture/hw2.sh,
linux_lecture/notes.txt
linux_lecture/hw.sh,
linux_lecture/homework.sh
(base) admin@MacBook-Pro cursor_git_hw % touch homework.sh
(base) admin@MacBook-Pro cursor_git_hw % stat homework.sh
16777221 36017740 -rw-r--r-- 1 admin staff 0 0 "Sep 18 15:27:34 2021" "Sep 18 15:27:34 2021" "Sep 18 15:27:34 2021" "Sep 18 15:27:34 2021" 4096 0 0 homework.sh
(base) admin@MacBook-Pro cursor_git_hw % touch -a-m-t homework.sh
touch: illegal option -- -
usage:
touch [-A [-][[hh]mm]SS] [-acfhm] [-r file] [-t [[CC]YY]MMDDhhmm[.SS]] file ...
(base) admin@MacBook-Pro cursor_git_hw % touch -a -m -t 202001010415.00 homework.sh
(base) admin@MacBook-Pro cursor_git_hw % stst homework.sh
zsh: command not found: stst
(base) admin@MacBook-Pro cursor_git_hw % stat homework.sh
16777221 36017740 -rw-r--r-- 1 admin staff 0 0 "Jan  1 04:15:00 2020" "Jan  1 04:15:00 2020" "Sep 18 15:50:51 2021" "Jan  1 04:15:00 2020" 4096 0 0 homework.sh
(base) admin@MacBook-Pro cursor_git_hw % touch hw1.sh hw2.sh hw3.sh hw1.txt
(base) admin@MacBook-Pro cursor_git_hw % find *.txt
hw1.txt
(base) admin@MacBook-Pro cursor_git_hw %
1
2
3
4
5
6
7
8
9
"homework.sh" 100L, 221B
(base) admin@MacBook-Pro cursor_git_hw % head homework.sh
1
2
3
4
5
7
(base) admin@MacBook-Pro cursor_git_hw % echo 'ls' >> notes.sh
(base) admin@MacBook-Pro cursor_git_hw % chmod +xnotes.sh
usage:  chmod [-fhv] [-R [-H | -L | -P]] [-a | +a | =a  [i][# [ n]]] mode|entry file ...
        chmod [-fhv] [-R [-H | -L | -P]] [-E | -C | -N | -i | -I] file ...
(base) admin@MacBook-Pro cursor_git_hw %
