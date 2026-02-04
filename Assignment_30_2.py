def main():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            word_count = 0
            for line in f:
                words = line.split()
                word_count += len(words)

        print("Number of words:", word_count)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
