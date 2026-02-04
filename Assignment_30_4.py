def main():
    src = input("Enter source file name: ")
    dest = input("Enter destination file name: ")

    try:
        with open(src, "r") as fsrc:
            data = fsrc.read()

        with open(dest, "w") as fdst:
            fdst.write(data)

        print("File copied successfully")

    except FileNotFoundError:
        print("Source file not found")

if __name__ == "__main__":
    main()