# welcome to the terminal 
### contents
- using this tutorial
- command structure
- getting help
- useful syntax & keybindings
- navigating filesystems
- running programs
- editing programs
- installing anaconda python

## using this tutorial
```git clone ...```
```cd ...```

## command structure
```prompt``` ```program``` ```options``` ```file input```
```[user@machine][~/Documents] $```vlc film.mp4```
options to programs are usually specified with ```-<letter>``` or ```--<word-no-spaces>```
```[james@thinkpad] [~] ❱❱``` ```pandoc -i readme.md -o readme.pdf --pdf-engine=xelatex```

## getting help
although options vary between programs, most programs have the option ```--help``` - which shows options. 
**try this:** browse the help sections for these common programs:
* ```ls```
* ```cd```
* ```cat```
* ```head```
```man``` is a program that displays a manual page for programs that have manuals. The manuals are generally comprehensive & concise, & can be all you need to learn about program. Bye google! try some of these:
* ```man man```
* ```man python```
* ```man ipython```

## useful syntax & keybindings
* ```clear``` or ```ctrl + l``` - clear text on screen
* ```<command> &``` run the command in the background - useful for commands that take a long time!
* ```ctrl + c``` - cancel command
* ```ctrl + shift + c``` copy text to clipboard - ```ctrl + shift + v``` to paste
* ```<tab>``` - autocomplete!! if there is >1 possible ending to the word (e.g. a program or file path) then double tap to see options
* ```*``` - wild card character. e.g. ```ls *.py``` will list any file that ends in ```.py``` 

## navigating filesystems
in unix systems, files are organized into a tree. check out the structure of this file system by running ```tree``` in this file system. the directory our shell is "in" is generally shown in the prompt. we can also check where we are by running ```pwd``` (print working directory). 
* **ls** - use ```ls``` to see the contents of the directory we're in, and ```ls -a``` to see hidden files (which start with a ```.```) ```ls -l``` shows us the long listing format of the files, which includes the permissions of the files (who can read, edit or execute), the file size in bytes (add the option ```-h``` to make the format more human readable), and the owners.
* **cd** - change directory. run ```cd <folder/directory>``` to change directory to a particular directory. ```cd ..``` takes us up a level in the file tree. we can jump to somewhere specific by specifying a full path like this: ```cd ~/documents/python-club/tutorials``` - autocomplete comes in really handy here. ```cd``` with no arguments takes us home. home (aka ```~```) is at ```/home/<your-username>```. the tilde ```~``` is a useful shortcut to writing /home/<your-username>```. try going up a few levels with ```cd ..``` - what's above us? how far can we go? what's at the root of the file system? how can we get home?
* ```mkdir <new-dir-name>``` - makes a new directory. try making a ```documents``` folder. ```rmdir <dir-name>``` will remove an empty directory.
* ```rm <file>``` - remove file. use ```rm -r <directory>``` to recursively remove the contents of a directory (& the directory itself)
* ```cp <file-to-copy> <destination-name>``` - copy a file - what does the ```-r``` option do?
* ```mv <file-to-move> <destination>``` - move a file. also used to rename a file.
* ```file <file-name>```

## running programs
some programs are already executable. ```ls -l``` shows us what is executable, e.g.
```-rwxr-xr-x 1 james james 16600 Dec  4 11:14 hello``` **come back to this**
run an executable like this ```./hello``` (if it's in your working directory, otherwise just give the path to the executable like ```../hello```). 
```hello``` is a binary file. you can tell by running ```file hello```. use ```cat``` to output the contents of the file to the terminal - what does it look like? nice? how about if we run ```hexdump hello```? 

I've put another program in the file system. can you find it? run it! what happens? what sort of file is it? use ```cat <file>``` to show the contents. what language is it? 

running ```python``` files :snake: -- if we don't have a shebang specifying which python interpreter to use (sometimes we have a few different ones installed), we can run a python file like ```python file.py```
## writing and editing programs
usually it's more practical to edit programs on your desktop with your favourite text editor, then copy the file to a server to run it. we'll cover this next time.

there are a lots of terminal-based text editors available. the easiest to use is ```nano```. to use nano, run ```nano <file-name>``` to either open an existing file, or create a new one if it doesn't already exist. The file extension will help nano decide which syntax highlighting to use. Use the arrow keys to move around, ```ctrl + o``` to save and ```ctrl +x``` to exit.

there's a python file in this file system. it contains errors. find it, correct the errors and run it!
