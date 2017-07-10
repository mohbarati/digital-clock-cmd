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
