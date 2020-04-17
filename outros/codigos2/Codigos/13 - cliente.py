from socket import socket, AF_INET, SOCK_STREAM

HOST = 'localhost'
PORT = 2223
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Mensagem do Cliente!')
data = s.recv(1024)
print data
s.close()
