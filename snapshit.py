import os
import hashlib
import argparse

def directory_list(path):
    directory=[]
    for dirpath, _, files in os.walk(path):
        for f in files:
            directory.append(os.path.join(dirpath, f))
    return directory

def generate_hash(path,dir,snapshit="snapshit.txt"):
    with open(snapshit,'w',encoding='utf-8') as output:
        for file in dir:
            hash = hashlib.sha256()
            BLOCK_SIZE = 65536
            print(file)
            with open(file,'rb') as f:
                for byte_block in iter(lambda: f.read(BLOCK_SIZE),b""):
                    hash.update(byte_block)
            output.write(file + "," + hash.hexdigest() + "\n")

def compare_string(string1,string2):
    if string1 == string2:
        print(f"string {string1} matches {string2}")
        toggle=1
        return toggle

def compare_files(file,file2):
    count=0
    with open(file, 'r') as string1_file:
            for string1 in string1_file:
                with open(file2, 'r') as string2_file:
                    match=0
                    for string2 in string2_file:
                        toggle=compare_string(string1.strip(),string2.strip())
                        if toggle==1:
                            match=1
                            count+=1
                    if match==0:
                        print(f"No match for {string1.strip()}") 
 

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--snapshit", help="specify new snapshit file name", action="store")
    parser.add_argument("-c", "--compare", help="specify file (or files) to compare", action="store")
    parser.add_argument("spath", help="Enter path to snapshit")
    parser.add_argument("dpath", help="Enter path to compare snapshit to",nargs='?')
    return parser.parse_args()


def main():
    args=parse_args()
    if args.snapshit:
        snapshit=args.snapshit
    else:
        snapshit="./snapshit.txt"
    if args.compare and not args.snapshit:
        snapshit="./cshit.txt"
    if args.dpath and args.compare:
        compare_files(args.spath,args.dpath)
    elif args.dpath and not args.compare:
        print("You can't specify a 2nd positional argument without -c")
        quit()
    else:
        dir=directory_list(args.spath)
        generate_hash(args.spath,dir,snapshit)
    if args.compare:
        compare_files("./snapshit.txt","./cshit.txt")

if __name__ == "__main__":
    main()
