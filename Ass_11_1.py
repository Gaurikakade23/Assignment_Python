def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    a = int(input("Enter Number: "))
    print("Prime Number" if is_prime(a) else "Not a Prime Number")

if __name__ =="__main__":
    main()