from cryptography.fernet import Fernet
import sys

def main(filename):
    key = Fernet.generate_key()
    with open(filename, 'wb') as f:
        f.write(key)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('provide encryption key file name as command line input!')
    else:
        main(sys.argv[1])
