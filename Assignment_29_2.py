def main():
    fname = input("Enter file name: ")

    try:
        fobj= open(fname, "r") 
        print("File opened successfully")
        print("Contents of the file:\n")
        print(fobj.read())

    except FileNotFoundError:
        print("File not found")

    finally:
        print("\nEnd of Application")

if __name__ == "__main__":
    main()
