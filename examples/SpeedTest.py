# SpeedTest.py

import socket
import time
from EasyGUI import *

Start = 0
Finish = 0

Open(4000)
Start = time.time()

for x in range(1,1340):
    Put('01=AAA~Left=' + str(x) + '~Height=100~Width=100~Back=255000000')
    Recv = Get()

for x in range(1,2210):
    Put('01=AAA~Top=' + str(x) + '~Height=100~Width=100~Back=255000000')
    Recv = Get()

Finish = time.time()
Tim = str(Finish - Start)
Put('02=BBB~Left=500~Top=1100~Width=900~Back=255255255~Text=3550 Itarations')
Put('02=CCC~Left=250~Top=1300~Width=1200~Back=255255255~Text=' + Tim + ' seconds')

print()

   
