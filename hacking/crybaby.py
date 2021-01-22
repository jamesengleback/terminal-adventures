import argparse
import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    encrypter = Fernet(key)
    with open(file_path, 'r') as f:
        file_contents = f.read()
    os.remove(file_path)
    with open(file_path + '.cry', 'wb') as f:
        f.write(encrypter.encrypt(file_contents.encode()))


def decrypt_file(file_path, key):
    encrypter = Fernet(key)
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    os.remove(file_path)
    with open(file_path, 'w') as f:
        f.write(encrypter.decrypt(file_contents).decode())

def read_key_file(key_file):
    with open(key_file, 'rb') as f:
        key = f.read()
    return key

def main(args):
    if os.path.exists(args.key):
        # if the key is a file
        key = read_key_file(args.key)
    else:
        # if the key is a command line argument (decoded string)
        key = args.key.encode()

    for i in os.walk(args.dir):
        directory = i[0]
        subdirs = i[1]
        files = i[2]
        for j in files:
            target_file = os.path.join(directory, j)
            if args.encrypt:
                encrypt_file(target_file, key)
            else:
                decrypt_file(target_file, key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    parser.add_argument('-k', '--key')
    parser.add_argument('-e', '--encrypt', action = 'store_true')
    args = parser.parse_args()
    main(args)
