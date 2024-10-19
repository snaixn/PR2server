import socket
import threading
host = '192.168.5.5'
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
nicknames = []
def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} покинул чат.'.encode('utf-8'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f'Подключен {str(address)}')
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Никнейм клиента: {nickname}')
        broadcast(f'{nickname} присоединился к чату!'.encode('utf-8'))
        client.send('Вы подключены к серверу!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print('Сервер запущен...')
receive()
