import socket

address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

my_socket = socket.socket(address_family, socket_type)
my_socket.connect(('data.pr4e.org', 80))

# HTTP 1.1: Host header
# https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.23
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

my_socket.send(request)

while True:
    buffer_size = 512
    data = my_socket.recv(buffer_size)

    if len(data) < 1:
        break

    print(data.decode())

my_socket.close()
