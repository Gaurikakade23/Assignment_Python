import sys

def main():
    try:
        source_file = sys.argv[1]
        dest_file = sys.argv[2]

        fobj= open(source_file, "r")
        data = fobj.read()

        nobj= open(dest_file, "w")
        nobj.write(data)

        print("File copied successfully")

    except IndexError:
        print("Please provide source and destination file names")
    except FileNotFoundError:
        print("Source file not found")
    finally:
        print("End of Application")

if __name__ == "__main__":
    main()
