EvenNum = lambda No : No % 2 == 0
def main():
    a = int(input("Enter Number: "))
    return EvenNum(a)  

if __name__ == "__main__":
    print(main())    