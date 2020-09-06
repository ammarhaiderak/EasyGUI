# Setup.py

import tkinter as tk
from tkinter import ttk  
from tkinter import *
import keyboard 
#import config
#from EasyGUI import * 

Keys = {'Up':0, 'Down':0, 'Right':0, 'Left':0}
ind = 1
LF = '\n'
root = tk.Tk()

def key_pressed(event):
    global ind
    
    if ind == 1:
        Keys["Up"] = event.keycode
        SM.set('Press Down arrow')
          
    if ind == 2:    
        Keys["Down"] = event.keycode S
        SM.set('Press Left arrow')
                
    if ind == 3:
        Keys["Left"] = event.keycode
        SM.set('Press Right arrow')
        
    if ind == 4:
        Keys["Right"] = event.keycode
        SM.set('Press Alt key')
    
    if ind == 4:
        root.destroy()
        f = open('config.py','w')
        f.write("Dict = {}" + LF)
        f.write("Row = {'Empty':'Empty'}" + LF)
        f.write("Lot = [Row]" + LF)
        f.write("W = 0 " + LF)
        f.write("H = 0 " + LF)
        f.write("IP = ''" + LF)
        f.write("Port = 0" + LF)
        f.write("SaveSw = False" + LF)
        f.write('Keys = ' + str(Keys) + LF)
        f.close()
    ind = ind + 1
    print('\a')
#    print(Keys)
    
SM = StringVar()
MoveLab=Label(root,  textvariable=SM, bg='#F0F0F0', fg='blue',  font=('arial', 16, 'bold')).place(x=10, y=60)
root.bind("<Key>",key_pressed)
SM.set('Press Up arrow')
print('\a')

root.mainloop()
