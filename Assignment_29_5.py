def main():
    fname = input("Enter file name: ")
    search_str = input("Enter string to search: ")

    try:
        with open(fname, "r") as f:
            data = f.read()

        count = data.count(search_str)

        print(f"'{search_str}' occurred {count} times in the file")

    except FileNotFoundError:
        print("File not found")

    finally:
        print("End of Application")

if __name__ == "__main__":
    main()
