"""
READ THIS:

    This is a digital clock that runs on your windows cmd (command window prompt).
    It should work on linux terminal too.
    To make it work, open up your Windows Command Prompt (or your linux bash terminal) and navigate
    to the folder where you have the following code saved as  somename.py  using cd command:
    for me it was like this: cd "C:\\Users\\Hosein\\Desktop" and then press enter. finally in the
    next line type: python somename.py    and press enter. enjoy.
""" 
# Note: I've assumed you have python 3.x installed and working.
# To END The Program Press: <Ctrl + c> 
import time, re
try:
    while True:
        
        time.sleep(1)
        
        m = re.search('..:..:..', time.asctime())   # Finding the time expression in time.asctime
        p = 'The time is: {} '.format(m.group(0))   # storing it in P
        print (p,end = '')                          # prints the time.
        
        print ('\b' * len(p),end = '',flush = True) # This is the most importans line. It deletes p 
                                                    # so you can print over its space on the screen.
        
except KeyboardInterrupt:                           # Ends the program is you press Ctrl + c.
    pass
finally:
    print ('(_______ HAVE A NICE TIME! :-) _______)')

'''
But if you wanna go one step further, you can write a batch script to run this code whenever and wherever you like with just a double click. this is my batch file for the task:(copy and past these two lines into a notepad file and then save and change the name of the file to somename.cmd)

MODE 25,7
call python "C:\\GIT\\TIME.py (change it with your own python file address)"

click on it and enjoy!
'''