def main():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            print("File contents:")
            for line in f:
                print(line, end="")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
