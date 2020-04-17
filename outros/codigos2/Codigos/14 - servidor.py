from socket import socket, AF_INET, SOCK_STREAM
HOST = ''
PORT = 2223
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) # Numero de Conexoes
conn, addr = s.accept()
data = conn.recv(1024)
print data
conn.send('Mensagem do Servidor!')
conn.close()
