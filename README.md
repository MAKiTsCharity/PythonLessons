# What is this the point here
The idea behind this repository is simple, I'll make different kinds of programs, with different kinds of python logic inside, and you'll be able to have a peek, look into them, and see how python functions.

I don't have a predetermined approach for you for how you should interract with this repo, so instead just have a look inside the folders, try to understand the code, if you can, try to write the program that does the same thing yourself, to see if you understand the logic


# What is needed
There effectively are three pieces of software that are needed in order for this to work

## Python
That's an obvious one. You can't run python without python. We write all code (in all different languages) in effectively a human language, a language computers can't understand, so in order to run the code we write, we'll need something to function as a "translator", or to put it another way, an "interpreter" (actual term for what python is)

Here's a link to download [python](https://www.python.org/downloads/)

## Git
Okay, neat, you can see this repo on github, but how to interract with it properly?

I mean, downloading each file one by one feels tedious so there has to be a better way, and won't you believe it, there is.

The reason why I'm hosting this on GIThub, in a GIT repository, is for you to be able to access it, using [GIT](https://git-scm.com/install/windows).

(we'll get to what git is in a second)

## Text editor

My personal editor of choice is [VSCode](https://code.visualstudio.com/download), but to be frankly honest, you can use whatever your heart desires.

## Additional

A terminal, linux has a terminal by default, windows doesn't, instead it has the disgusting "Command line", yuck, but you can install a terminal on windows just fine, would recommend

# Cheat sheet

The cheat sheet we'll do out of order, because this matters differently, so first

## Terminal

Once you open a terminal, you can think about it like opening a file explorer, on the left you should see the path of where you are on your computer, so stuff like `C:\Users\handsome\Desktop` on windows, or something like `/home/handsome` on linux, now, that's the folder (also called a "directory") you're in, if you'd like to list all the files in that directory, the command is `ls` which does stand for "list". If you'd like to change the directory, you use the "change directory" command, so for example `cd folderName`.

For all the commands, when you're asked to provide a path, you do it by... well... providing a path. In the paths a single dot `.` stands for "current directory" and double dot `..` stands for "directory above current directory".

So if you're in a `/firstFolder/second/Third/` and you `cd ../..` then you'll end up in `/firstFolder/`.

If you then `cd ./second/` you'll end up in `/firstFolder/second/`

Simple as it could be

Also, there is the `mkdir SOMETHING` which stands for "make directory".

## Git

In order to start our project we'd like to first clone the repository, which we can do using the `git clone <REPO>` command, now, it should be noted that once you run this command, it will clone the repository into the folder you're currently in, and once you run it with this very repository as your input, so `git clone https://github.com/MAKiTsCharity/PythonLessons.git`, you should see "PythonLessons" folder appear.

Now, you can enter that folder using the `cd ./PythonLessons/`, and there you are, you have the repository.

I will myself update this repository in the future, so if you'd like a single command that will update this repository for you, then you're in luck, because `git pull` exists... it really is that simple.

For future reference, if you'd like to use git yourself, you can also `git commit` to kind of "save your changes", with `-a` flag to add "all" and `-m` flag to add a "message". So for example `git commit -a -m "name of commit"`

There's also `git add .` to add different files to your repo (basically telling git to keep track of it) with a flag `-A` to add all of them (yes, for this command it has to be a capital A, go figure).

There are more commands, like to switch between commits, between branches, create new branches, initialise a repository, but you can figure all of that out on your own, just `git help`

## Python

And then finally, python.

Python you can run on its own `python`, or you can tell it to run a specific file `python ./path/to/file.py`.

There really isn't much more to it, and I think it should be left blank for now, you'll understand this better as we continue working through the folders.

# FAQ