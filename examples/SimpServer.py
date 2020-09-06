# SimpServer.py
import config 
from EasyGUI import *
    
Open(4000)

while True: 
    Mess = input('Send: ')
    Put(Mess)
    print(Get())
