import socket
import os
import sys
import time

HOST = socket.gethostbyname(socket.gethostname())
if len(sys.argv) == 1:
    PORT = 5050
else:
    PORT = sys.argv[1]

def main():
    print(HOST, PORT)

    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen(5) # number of connection attempts bedore refusing access
        connection, address = s.accept()
        ###
        stay_open = True
        while stay_open:
            i = input('>> ')
            if i == 'exit':
                stay_open = False
            connection.send(str.encode(i))
            timer_start = time.time()            
            try:
                response = connection.recv(1024).decode()
                print(response)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    main()
