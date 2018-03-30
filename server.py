import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12348
s.bind(('192.168.0.100', port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  for i in range(1,1000):
      string = 'Thank you for connecting!\n'+ str(i)
      c.send(string)
  c.close()
