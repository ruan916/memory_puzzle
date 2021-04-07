import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 12000))

while True:
    bytes_message, client_ip_address = server.recvfrom(2048)
    answer_message = bytes_message.decode().upper()
    server.sendto(answer_message.encode(),client_ip_address)
    print(answer_message)