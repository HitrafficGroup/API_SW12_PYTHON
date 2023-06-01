import socket
import sys  
frame1 = bytearray(13)
frame1[0] =192
frame1[1] =16
frame1[2] =32
frame1[3] =16
frame1[4] =3
frame1[5] =1
frame1[6] =1
frame1[7] =0
frame1[8] =128
frame1[9] =7
frame1[10] =0
frame1[11] =204
frame1[12] =192


host = 'controlador'
port = 4001  # web

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address') 
remote_ip = '192.168.2.97'

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print('# Sending data to server')

try:
    s.sendall(frame1)
    reply = s.recv(1024)
    data = list(reply)
    print(data)
except socket.error:
    print('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')

