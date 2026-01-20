def Pallindrom(num):
    original = num
    pd =0

    while num!=0:
        digit = num%10
        pd = pd*10 +digit
        num //=10
    if original == pd:
        print("Palindrom")
    else:
        print("Not Palindrom")    
def main():
    a =int(input("Enter number: "))
    Pallindrom(a)

if __name__ == "__main__":
    main()    