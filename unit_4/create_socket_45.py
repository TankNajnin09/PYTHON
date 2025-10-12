import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = 'localhost'
port = 5000  # Arbitrary non-privileged port

# Bind the socket to the port
s.bind((host, port))

# Start listening for connections
s.listen(5)

print(f"Socket created successfully and listening on {host}:{port}")
