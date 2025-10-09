# a server that sends file contents to client
import socket

# take server name and port number
host = 'localhost'
port = 6767

# create TCP socket
s = socket.socket()

# bind socket to host and port number
s.bind((host, port))

# maximum 1 connection is accepted
s.listen(1)

# wait till client accepts a connection
c, addr = s.accept()
print("A client accepted connection")
# accepts file name from client
fname = c.recv(1024)

# convert file name into normal string
fname = str(fname.decode())
print("File name received from client: " + fname)

try:
    # open the file at sever side
    f = open(fname, 'rb')

    # read content of the file
    content = f.read()

    # send file content to client
    c.send(content)
    print("File content send to client")

    # close the file
    f.close()
except FileNotFoundError:
    c.send(b'File does not exist')
# disconnect server
c.close() 