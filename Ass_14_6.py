OddNum = lambda No : No % 2 != 0
def main():
    a = int(input("Enter Number: "))
    return OddNum(a)  

if __name__ == "__main__":
    print(main())    