
# digital-clock-cmd
 This is just a simple digital clock, more importantly i have to learn github!☻
 The most important part of this code is where i used <'\b' * len(p)> to erase the
 printed text from screen (it can not be done if there's a return key at the end of
 printed expression).
 
 the .cmd file is a batch script to make an excecutable file (in windows). 
 this is my batch file for the task:(copy and past these two lines into a
 notepad file and then save and change the name of the file to somename.cmd)


MODE 25,7

call python "C:\\GIT\\TIME.py (change it with your own python file address)"

