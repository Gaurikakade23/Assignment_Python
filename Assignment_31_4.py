import os

LOG_FILE = "automation.log"

def write_log(msg):
    f = open(LOG_FILE, "a")
    f.write(msg + "\n")
    f.close()

def copy_files_by_ext(src, dest, ext):
    if not os.path.exists(src):
        raise Exception("Source directory not found")

    if not os.path.isdir(src):
        raise Exception("Source is not a directory")

    if not os.path.exists(dest):
        os.mkdir(dest)
        write_log("Created directory: " + dest)

    for file in os.listdir(src):
        if file.endswith(ext):
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
        ext = input("Enter extension: ")

        copy_files_by_ext(src, dest, ext)
        write_log("Copy by extension completed")

    except Exception as e:
        write_log("Error in CopyExt: " + str(e))

main()
