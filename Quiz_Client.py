import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = "127.0.0.1"
port = 8000

nick_name = input('How would you like to be called: ')
print('Connected with the server')

client.connect((address, port))

def recieve():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nick_name.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error occured!')
            client.close()
            break

def write():
    while True:
        message = '{} : {}'.format(nick_name , input(''))
        client.send(message.encode('utf-8'))

recieve_thread = Thread(target=recieve)
recieve_thread.start()

write_thread = Thread(target=write)
write_thread.start()