import socket

ip = input("Enter server ip: ")
host = ip
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print("You are connected to the server\n")
while 1:
     data = s.recv(1024).decode('utf-8')
     print('Server: ' + data)
     if(data == "cmdclose"):
          break
