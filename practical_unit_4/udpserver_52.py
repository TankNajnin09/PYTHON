# a UDP server that sends messages to client 
import socket 
import time

# take the server name and port number 
host = 'localhost' 
port = 5000

# Create a socket at server side to use UDP protocol 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# let the server waits for 5 seconds 
time.sleep(5)

# send messages to the client after encoding into binary string 
s.sendto(b"Hello client, how are U", (host, port))
msg = "Bye!" 
s.sendto(msg.encode(), (host, port))

# disconnected the server 
s.close()
