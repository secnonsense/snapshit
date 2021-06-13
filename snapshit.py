import os
import hashlib

def directory_list(path):
    dir = next(os.walk(path))[2]
    return dir

def generate_hash(path,dir):
    hash = hashlib.sha256()
    BLOCK_SIZE = 65536
    for file in dir:
        print(path+file)
        with open(path+file,'rb') as f:
            for byte_block in iter(lambda: f.read(BLOCK_SIZE),b""):
                hash.update(byte_block)
            print (file,hash.hexdigest())

def main():
    path="/Users/scott/scripts/"
    dir=directory_list(path)
    generate_hash(path,dir)

if __name__ == "__main__":
    main()
