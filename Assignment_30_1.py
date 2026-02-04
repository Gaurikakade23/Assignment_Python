def main():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            line_count = 0
            for _ in f:
                line_count += 1

        print("Number of lines:", line_count)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
