# a server that receives and sends messages - save this as chatserver.py
import socket
host = '127.0.0.1'
port = 9000
# create server side socket
s = socket.socket()
s.bind((host, port))
# let maximum number of connections are 1 only
s.listen(1)
# wait till a client connects
c, addr = s.accept()
print("A Client connected")
# server runs continuously
while True:
    # receive data from client
    data = c.recv(1024)

    # if client sends empty string, come out
    if not data:
        break
    print("From client: " + str(data.decode()))

    # enter response data from server
    data1 = input("Enter Response : ")

    # send that data to client
    c.send(data1.encode())

    # close connection
c.close()