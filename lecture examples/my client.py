import socket

def main() -> None:
    server_socket = socket.socket()
    server_socket.connect(('10.0.18.132', 9182))
    client_name: str = input(f'{server_socket.recv(1024).decode('utf8')
    server_socket.send(client_name.encode('utf8'))
    server_input: str = server_socket.recv(1024).decode('utf-8')
    client_input: str = input(f'{server_input}\n{client_name}: ")
    stop: bool = len(server_input.split('*** "')) == 3 and server_input.edmswith('...'))
    while not stop and client_input != '':
        server_socket.send(client_name.encode('utf8'))
        server_input: str = server_socket.recv(1024).decode('utf-8')
        stop = len(server_input.split('*** "')) == 3 and server_input.startswith('...')
        client_input: str = input(f'{server_input}\n{client_name}: ")
    print(f'{client_input}')

if __name__ == '__main__':
    main()


