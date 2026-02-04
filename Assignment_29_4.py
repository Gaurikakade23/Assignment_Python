import sys

def main():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        with open(file1, "r") as f1, open(file2, "r") as f2:
            data1 = f1.read()
            data2 = f2.read()

        if data1 == data2:
            print("Success: Both files have the same contents")
        else:
            print("Failure: Files contents are different")

    except IndexError:
        print("Please provide two file names from command line")
    except FileNotFoundError:
        print("One or both files not found")
    finally:
        print("End of Application")

if __name__ == "__main__":
    main()
