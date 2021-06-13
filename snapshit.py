import os
import hashlib
import argparse

def directory_list(path):
    dir = next(os.walk(path))[2]
    return dir

def generate_hash(path,dir,snapshit="snapshit.txt"):
    with open(snapshit,'w',encoding='utf-8') as output:
        for file in dir:
            hash = hashlib.sha256()
            BLOCK_SIZE = 65536
            print(path+file)
            with open(path+file,'rb') as f:
                for byte_block in iter(lambda: f.read(BLOCK_SIZE),b""):
                    hash.update(byte_block)
            output.write(file + "," + hash.hexdigest() + "\n")

def compare_files(file,file2,nomatch=0,i=0,d=0,x=0):
    count=0
    with open(file, 'r') as string1_file:
            for string1 in string1_file:
                with open(file2, 'r') as string2_file:
                    match=0
                    for string2 in string2_file:
                        toggle=compare_string(string1.strip(),string2.strip(),nomatch,i,d,x)
                        if toggle==1:
                            match=1
                            count+=1
                    if match==0 and nomatch==1:
                        print(f"No match for {string1.strip()}") 
                    elif match==0 and d==1:
                        print(string1.strip())
    if i==1 or d==1:
        print("\n")
    else:
        print(f"\nTotal Matches: {count}\n")    

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
    dir=directory_list(args.spath)
    generate_hash(args.spath,dir,snapshit)

if __name__ == "__main__":
    main()
