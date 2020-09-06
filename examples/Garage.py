# Garage.py 
import time
from EasyGUI import *
import config 
def GoUp():
    for n in range(400,0,-10):
        time.sleep(.1)
        Send('11=door~Height=' + str(n))
    Send('01=up~Text=DOWN')    
def GoDown():
    for n in range(0,480, +10):
        time.sleep(.1)
        Send('11=door~Height=' + str(n))
    Send('01=up~Text=UP')    
Open(4000)
Send('51=Load~Text=Garage.dat')
time.sleep(.5)
while True:
    Wait()
    GoUp()
    Wait()
    GoDown()
