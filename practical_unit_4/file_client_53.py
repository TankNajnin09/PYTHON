# a client that sends and receives data
import socket

# take server name and port number
host = 'localhost'
port = 6767

# create a tcp socket
s = socket.socket()

# connect to server
s.connect((host, port))

# type file name from the keyboard
filename = input("Enter file name : ")
# send the file name to the server
s.send(filename.encode())
# receive file content from server
content = s.recv(1024)
print(content.decode())
# disconnect the client
s.close()