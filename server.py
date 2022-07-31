import socket

# Встановлюємо максимальне число UDP пакета
UDP_MAX_SIZE = 65535


# Функція для запуску сервера яка прийматиме host і port
def listen(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))
    print(f'Listening at {host}:{port}')

    members = []  # список підключений клієнтів
    # Постійний цикл для слухання клієнтів і відправлення повідомлень
    while True:
        msg, addr = s.recvfrom(UDP_MAX_SIZE)

        # Перевірка якщо клієнт відсутній то його дотати
        if addr not in members:
            members.append(addr)

        if not msg:
            continue

        client_id = addr[1]
        if msg.decode('ascii') == '__join':
            print(f'Client {client_id} joined chat')
            continue

        msg = f'client{client_id}: {msg.decode("ascii")}'
        for member in members:
            if member == addr:
                continue

            s.sendto(msg.encode('ascii'), member)


if __name__ == '__main__':
    listen()
