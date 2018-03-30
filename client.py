import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12348

s.connect(('192.168.0.100', port))
print (s.recv(65000))
s.close
