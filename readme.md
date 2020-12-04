# welcome to the terminal 
### contents
- using this tutorial
- command structure
- useful syntax & keybindings
- getting help
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
