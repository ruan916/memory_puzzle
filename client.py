import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    submit_message = input("Digite a mensagem desejada: ")
    client.sendto(submit_message.encode(),("192.168.0.100", 12000))
    bytes_message, server_ip_address = client.recvfrom(2048)
    print(bytes_message.decode())