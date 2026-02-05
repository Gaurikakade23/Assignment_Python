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

def FindDuplicates(DirectoryName):
    try:
        validate_directory(DirectoryName)
        write_log("Duplicate search started")

        Duplicate = {}

        for FolderName, SubFolder, FileName in os.walk(DirectoryName):
            for fname in FileName:
                fname = os.path.join(FolderName, fname)
                CheckSum = CalculateCheckSum(fname)

                if CheckSum in Duplicate:
                    Duplicate[CheckSum].append(fname)
                else:
                    Duplicate[CheckSum] = [fname]

        for key in Duplicate:
            if len(Duplicate[key]) > 1:
                for file in Duplicate[key]:
                    write_log("DUPLICATE: " + file)

    except Exception as e:
        write_log(str(e))

def main():
    try:
        if len(os.sys.argv) != 2:
            raise Exception("Usage: DirectoryDuplicate.py <DirectoryName>")
        FindDuplicates(os.sys.argv[1])
    except Exception as e:
        write_log(str(e))

if __name__ == "__main__":
    main()
