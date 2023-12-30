import socket

# Функція для надсилання повідомлення
def send_message(sock, message):
    # Обчислюємо довжину повідомлення
    message_length = len(message)
    # Відправляємо довжину повідомлення в 4 байтах
    sock.send(message_length.to_bytes(4, byteorder='big'))
    # Відправляємо саме повідомлення
    sock.send(message.encode())

# Функція для отримання повідомлення
def receive_message(sock):
    # Отримуємо довжину повідомлення (4 байти)
    message_length_bytes = sock.recv(4)
    message_length = int.from_bytes(message_length_bytes, byteorder='big')
    # Отримуємо саме повідомлення
    message = sock.recv(message_length)
    return message.decode()

# Адреса та порт для спілкування
HOST = 'localhost'
PORT = 12345

# Створюємо серверний сокет та очікуємо на підключення
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Сервер очікує на підключення...")
client_socket, addr = server_socket.accept()
print("З'єднано з клієнтом:", addr)

# Створюємо клієнтський сокет та підключаємося до сервера
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Підключено до сервера:", (HOST, PORT))

# Надсилаємо та отримуємо 100 повідомлень
for i in range(100):
    message_to_send = f"Повідомлення #{i}"
    send_message(client_socket, message_to_send)
    received_message = receive_message(client_socket)
    print(f"Відправлено: {message_to_send}, Отримано: {received_message}")

# Завершуємо з'єднання
client_socket.close()
server_socket.close()
