import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5059

def main():
    print(HOST, PORT)

    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen(5) # number of connection attempts bedore refusing access
        connection, address = s.accept()
        ###
        stay_open = True
        while stay_open:
            i = input()
            if i == 'exit':
                stay_open = False
            connection.send(str.encode(i))
            response = connection.recv(1024).decode()
            print(response)


if __name__ == '__main__':
    main()
