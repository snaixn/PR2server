import socket
import threading
nickname = input("Выберите никнейм: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.5.5'
port = 12345
client.connect((server_ip, port))
sent_messages = []
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                if message not in sent_messages:
                    print(message)
        except:
            print("Произошла ошибка.")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        sent_messages.append(message)
        client.send(message.encode('utf-8'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()