# GUIfy.py 
import os
from os import path
import socket
import sys    
import time
from tkinter import messagebox
import config  
 
CRLF = '\r\n'
LF = '\n'
Eq = '='
Sep = '~'
s = socket


def FileExist(FileName):
    if path.exists(FileName):
        return True
    else:
        return False 

def Open(Port):
    global conn
    global s
    hostname = socket.gethostname()
    config.IP = socket.gethostbyname(hostname)
    config.Port = Port 
    print(config.IP + ':' + str(config.Port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create Socket
    s.bind(('',Port))
    s.listen(10)                               # Wait for Client to connect
    print ('Listening on Port ' + str(Port))
    conn, addr = s.accept() 
    print(addr)
      
    x = (Get())                                                   # Read sign on from Client
    y = x.split(': (')                                            # store screen dimensions
    x = y[1]
    x = x.split('x')
    
    config.W = x[0]
    config.H = x[1] 
    print(config.W, 'x', config.H) 
#---------------------------------------------------------------------------
def Convert(L):                                                   # Convert List to Dictionary
    res_dct = {L[i]: L[i + 1] for i in range(0, len(L), 2)}
    return res_dct
#---------------------------------------------------------------------------
def Put(mess):
        config.SaveSw = True 
        L = []
        conn.send((mess + CRLF).encode())             # Send message to server
    
        if mess == 'Exit':
            return
        if len(mess) < 3:  
            return 
        if mess[0:2] > '49':                          # don't change directories 
            return                                    # these are file commands
        mess = mess.replace('~','=')                  # replace ~ with =
        mess = mess.strip('\\n')
        L = mess.split('=')                           # move it to a List
        L[0], L[1] = L[1],L[0]                        # swap ID with type
        config.Dict = {}                              # clear Dict
        config.Dict = {**config.Dict, **Convert(L)}   # convert list to dict
        
        sw = 0
        for config.Row in config.Lot:                 # loop through each dictionary
            if L[0] in config.Row:                    # does it exist ?
                sw = 1
                config.Row.update(config.Dict)        # found it - update it
            
        if sw == 0:    
            config.Lot.append(config.Dict)            # Does not exist - append to List
#....................................................................   
def Get():
    recv = conn.recv(1024).decode()               # Receive message from Client
    if recv == '99':
        messagebox.showinfo("Warning", "Invalid Command !")    
    return(recv)
#---------------------------------------------------------------------------
def Send(mess):
    Put(mess)
    recv = conn.recv(1024).decode()               # Receive message from Client
    return(recv)    
#---------------------------------------------------------------------------
def GetForm(FileName):
    global FileTransferPort
    global Tot 
    global CRLF
      
    CRLF = '\r\n' 
    FileTransferPort=8008  
    Put('56=CopyFrom~Text=' + FileName + '~Left=' + str(FileTransferPort)) #from Client
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create Socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse the portt.
    s.bind(('',FileTransferPort))
    s.listen(10)                                 # Wait for Client to connect
#    print ('File TransferSocket now listening on port ' + str(FileTransferPort))
    conn, addr = s.accept()
    
    Recv = conn.recv(1024).decode()
    
    if Recv[0:2] == '96':
        messagebox.showinfo("Warning", "File does not exist !")
        return
    
    if len(Recv)>=2 and Recv[0:2]=='40':  
        Tot = ''
        while True: 
            data = conn.recv(1024)
            Tot = Tot + data.decode('ascii')
            if not data:    
                break   
    conn.close()
    s.close()
    
#    print('File Transfer socket closed!\n')
    lines = Tot.splitlines()
    for line in lines:
        if line != '':
            Put(line)
            Get()
            time.sleep(0.05)
#---------------------------------------------------------------------------
def Find(ID, Kex):
    for x in config.Lot: 
        if ID in x: 
            return x.get(Kex) 
    else:
        return ''                                                                                                      
#---------------------------------------------------------------------------       
def Wait():
    conn.send(('40' + CRLF).encode())        # Send message to server
    reply = conn.recv(1024).decode()         # Receive message from Client
    reply = reply.strip('\n\r') 
    return(reply)
#---------------------------------------------------------------------------       
                 
def Switch(a):                              #switches the first parameter of every line
    x = a.find('~') 
    y = a[0:x]
    a = a.replace(y,'')  
    x = y.find('=')
    x = y[0:x]
    one = x
    x = y.find('=')
    two = y.replace(one + '=','')
    a = two +'=' + one + a
    return a       
       
       
       
       