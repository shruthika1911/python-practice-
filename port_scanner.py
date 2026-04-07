import socket

target = "127.0.0.1" # your own computer
port = 80 # checking port 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = s.connect_ex((target, port))

if result == 0:
    print("Port is open")
else:
    print("Port is closed")

s.close()
