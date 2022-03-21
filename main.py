
#It's a memory game

#There will be an array of LEDs of different colours they will randomly blink one after the other for a number of times

#Then once it stops, the user has to enter the order in which they blinked ( like red, green,red, yellow,green)

#If the user has inputted correctly he will continue to the next level (the time interval will be lesser and there will be more no of blinks)

#If he inputs incorrectly, he will lose the game

#import all necessary modules
from tkinter import *

#import pyfirmata module
from pyfirmata import Arduino, util
import random
import time

red=1
green=2
blue=3
yellow=4
orange=5


#welcome and rules
rules=Tk()
rules.title('RULES')
rule=Label(rules,text='''WELCOME TO OUR MEMORY GAME


    THE LEDs WILL BLINK RANDOMLY FOR
 A NO OF TIMES YOU HAVE
 TO REMEMBER THE ORDE IN WHICH THEY BLINK AND
 ENTER THEM IN THE CORRECT ORDER''',padx=200,pady=150,bg='pink',fg='black',font=('impact',28))
rule.pack()
rules.after(6000, lambda: rules.destroy())
rules.mainloop()

#tell that the LEDs will blink now
blink=Tk()
blink.title('BLINKING NOW')
b=Label(blink, text='''The LEDs will blink now,
    remember their order''', font=('arvo',32),padx=200,pady=150,bg='purple',fg='pink')
b.pack()
blink.after(2500, lambda: blink.destroy())
blink.mainloop()

#give a pause of 1,5 sec
time.sleep(1.5)

#define the arduino board
board=Arduino('COM8')

#start
print('WELCOME TO THE LED MEMORY GAME!!!')

#level one
print('LEVEL ONE ')

random_list = []

#blinking  // LEVEL 1
#blink the led
for i in range(6):
    
    n=random.randint(2,6)
    
    board.digital[n].write(1)
    time.sleep(0.7)
    board.digital[n].write(0)
    time.sleep(0.7)
    
    random_list.append(n-1)

print(random_list)



#list appending functions
def r(lst):
    lst.append(red)

def b(lst):
    lst.append(blue)

def g(lst):
    lst.append(green)

def y(lst):
    lst.append(yellow)

def o(lst):
    lst.append(orange)

user_list=[]


#tkinter window
root=Tk()
root.title('LED Memory Game')
Welcomemessage=Label(root,text='WELCOME',fg='lightblue',bg='purple',font='impact',padx=300,pady=50)
Scoreboard=Label(root,text='Score',fg='black',bg='pink',padx=50,pady=100)

#window closing function
def close():
    root.destroy()
#buttons

Red=Button(root,text='Red',bg='red',fg='yellow',command= lambda : user_list.append(1), padx=30,pady=30)
Blue=Button(root,text='Blue',bg='blue',fg='white',command=lambda : user_list.append(2),padx=30,pady=30)
Green=Button(root,text='Green',bg='green',fg='white',command=lambda : user_list.append(3),padx=30,pady=30)
Yellow=Button(root,text='Yellow',bg='yellow',fg='red',command=lambda: user_list.append(5),padx=30,pady=30)
Orange=Button(root,text='Orange',bg='orange',fg='blue',command=lambda: user_list.append(4),padx=30,pady=30)
ENTER=Button(root,text='ENTER',bg='magenta',fg='white',padx=30,pady=20,command=close)

#geometry/arrangement
Levelboard=Label(root,text='Level',fg='black',bg='white',padx=50,pady=100)
Welcomemessage.grid(row=0,column=1)
Scoreboard.grid(row=1,column=0)

Red.grid(row=2,column=1)
Blue.grid(row=3,column=1)
Green.grid(row=4,column=1)
Orange.grid(row=5,column=1)
Yellow.grid(row=6,column=1)

Levelboard.grid(row=1,column=2)

ENTER.grid(row=0,column=0)

#window mainloop
root.mainloop()

#port = 'COM4'
#board = pyfirmata.Arduino(port)



led_list = [red, green, blue, yellow, orange]




print(user_list)

if random_list==user_list:
    win=Tk()
    win.title('WIN')
    w=Label(text='''CONGRATULATIONS!!!

        YOU HAVE WON !
        PROCEED TO THE NEXT LEVEL''',bg='pink',fg='black',font=('sans-serif',36),padx=300,pady=200)
    w.pack()
    win.mainloop()
else:
    lose=Tk()
    lose.title('LOSE')
    l=Label(text='''SORRY ):

        YOU HAVE LOST !
        PLEASE TRY AGAIN''',bg='pink',fg='black',font=('sans-serif',36),padx=300,pady=200)
    l.pack()
    lose.after(2500, lambda: lose.destroy())
    lose.mainloop()
    exit()



