import socket

address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

my_socket = socket.socket(address_family, socket_type)
my_socket.connect(('data.pr4e.org', 80))

request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'

# When we talk to an external resource like a network socket we send bytes,
# so we need to encode Python strings into a given character encoding.
request_in_bytes = request.encode()

my_socket.send(request_in_bytes)

while True:
    buffer_size = 512
    data_in_bytes = my_socket.recv(buffer_size)

    if len(data_in_bytes) < 1:
        break

    # When we read data from external resource, the data comes to us in bytes.
    # That's why we need to decode it, so it's represented as a string instead.
    print(data_in_bytes.decode())

my_socket.close()
