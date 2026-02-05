import os
import time
import hashlib

LOG_FILE = "Log.txt"

def write_log(msg):
    f = open(LOG_FILE, "a")
    f.write(msg + "\n")
    f.close()

def validate_directory(DirectoryName):
    if not DirectoryName:
        raise Exception("Directory name not provided")
    if not os.path.exists(DirectoryName):
        raise Exception("Directory does not exist")
    if not os.path.isdir(DirectoryName):
        raise Exception("Not a directory")

def CalculateCheckSum(fname):
    hobj = hashlib.md5()
    f = open(fname, "rb")
    while True:
        buffer = f.read(1024)
        if not buffer:
            break
        hobj.update(buffer)
    f.close()
    return hobj.hexdigest()

def DirectoryChecksum(DirectoryName):
    try:
        validate_directory(DirectoryName)
        write_log("Checksum process started")

        for FolderName, SubFolder, FileName in os.walk(DirectoryName):
            for fname in FileName:
                fname = os.path.join(FolderName, fname)
                CheckSum = CalculateCheckSum(fname)
                write_log(fname + " => " + CheckSum)

    except Exception as e:
        write_log(str(e))

def main():
    try:
        if len(os.sys.argv) != 2:
            raise Exception("Usage: DirectoryChecksum.py <DirectoryName>")
        DirectoryChecksum(os.sys.argv[1])
    except Exception as e:
        write_log(str(e))

if __name__ == "__main__":
    main()
