import os

LOG_FILE = "automation.log"

def write_log(msg):
    f = open(LOG_FILE, "a")
    f.write(msg + "\n")
    f.close()

def rename_files(directory, old_ext, new_ext):
    if not os.path.exists(directory):
        raise Exception("Directory not found")

    if not os.path.isdir(directory):
        raise Exception("Not a directory")

    for file in os.listdir(directory):
        if file.endswith(old_ext):
            old_path = os.path.join(directory, file)
            new_name = file.replace(old_ext, new_ext)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            write_log("Renamed: " + file + " -> " + new_name)

def main():
    try:
        directory = input("Enter directory name: ")
        old_ext = input("Enter old extension: ")
        new_ext = input("Enter new extension: ")

        rename_files(directory, old_ext, new_ext)
        write_log("Rename operation completed")

    except Exception as e:
        write_log("Error in Rename: " + str(e))
if __name__ =="__main__":
    main()
