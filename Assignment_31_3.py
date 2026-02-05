import os

LOG_FILE = "automation.log"

def write_log(msg):
    f = open(LOG_FILE, "a")
    f.write(msg + "\n")
    f.close()

def copy_all_files(src, dest):
    if not os.path.exists(src):
        raise Exception("Source directory not found")

    if not os.path.isdir(src):
        raise Exception("Source is not a directory")

    if not os.path.exists(dest):
        os.mkdir(dest)
        write_log("Created directory: " + dest)

    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dest_path = os.path.join(dest, file)

        if os.path.isfile(src_path):
            data = open(src_path, "rb").read()
            open(dest_path, "wb").write(data)
            write_log("Copied: " + file)

def main():
    try:
        src = input("Enter source directory: ")
        dest = input("Enter destination directory: ")

        copy_all_files(src, dest)
        write_log("Copy operation completed")

    except Exception as e:
        write_log("Error in Copy: " + str(e))

if __name__ == "__main__":
    main()    
