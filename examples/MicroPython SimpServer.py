#MicroPython SimpServer
import sys
import socket
CRLF = '\r\n'
port = 4000 
s = socket;

def Put(mess):
    c.send((mess + CRLF).encode())              # Send message

def Get():
    return c.recv(1024).decode()                # Read reply

def Open(port):
    global c
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( ('', port) )
    s.listen(10)
    print ('Listening on Port ' + str(port))
    c, a = s.accept()
    print ('Client connected', a)
    print(Get())

def Close():                                    # Close Socket
    c.close()
    s.close()

def Start():
    Open(port)                                  # Open Socket 
    Put('51=Load~Text=Sample.dat')              #Load from Client  
    print(Get())
    
Start()
while True:
    Put('40')                                   # wait fro Client's reply
    rec = Get()
    
    if (rec == '40=Radio~2'):                   # Finish, close
       Put('Exit')
       Close()
       print('Socket Closed')
       sys.exit()
       
    if (rec == ''):                             # Client off line
        Close()                                 # Close socket
        print('Reopening')
        Start()                                 # Reopen Socket
    print(rec)
       
       