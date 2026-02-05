import os

LOG_FILE = "automation.log"

def write_log(msg):
    f = open(LOG_FILE, "a")
    f.write(msg + "\n")
    f.close()

def search_files(directory, ext):
    if not os.path.exists(directory):
        raise Exception("Directory not found")

    if not os.path.isdir(directory):
        raise Exception("Not a directory")

    found = False
    for file in os.listdir(directory):
        if file.endswith(ext):
            write_log("Found file: " + file)
            found = True

    if not found:
        write_log("No files found with extension " + ext)

def main():
    try:
        directory = input("Enter directory name: ")
        ext = input("Enter file extension: ")

        search_files(directory, ext)

    except Exception as e:
        write_log("Error in FileSearch: " + str(e))

if __name__ == "__main__":
    main()
