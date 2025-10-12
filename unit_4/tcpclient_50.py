# a TCP/IP client that receives messages from server 
import socket

# take the server name and port number 
host = 'localhost' 
port = 5000

# create a client side socket using TCP/IP protocol 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port number 
s.connect((host, port))

# receiving message string from server, at a time 1024 B 
msg = s.recv(1024)

# repeat as long as message strings are not empty 
while msg:
    print("Received : " + msg.decode())
    msg = s.recv(1024)

# disconnected the client 
s.close() 
