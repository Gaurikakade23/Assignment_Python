def main():
    fname = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        with open(fname, "r") as f:
            data = f.read()

        count = data.count(word)
        print(f"'{word}' found {count} times")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
