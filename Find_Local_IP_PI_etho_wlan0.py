import socket
import fcntl
import struct

s = socket.socketpair(socket.AF_INET, socket.SOCK_DGRAM)
try:
    ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack(b'256s', b'etho'[:15]))[20:24])
except IOError:
    pass
try:
    ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack(b'256s', b'wlan0'[:15]))[20:24])
except IOError:
    pass

print(ip)
