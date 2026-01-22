def Perfect_No(num):
    if num <= 0:
        return False

    sum_div = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_div += i

    return sum_div == num


def main():
    a = int(input("Enter Number: "))

    if Perfect_No(a):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()
