import threading

def Prime(numbers):
    prime_list = []

    for num in numbers:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)

    print("Prime numbers:", prime_list)


def NonPrime(numbers):
    nonprime_list = []

    for num in numbers:
        if num <= 1:
            nonprime_list.append(num)
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    nonprime_list.append(num)
                    break

    print("Non-prime numbers:", nonprime_list)


def main():
    Data = [10, 11, 12, 13, 14, 17, 18, 19, 20]

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()
