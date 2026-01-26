import threading

def SumElements(numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum of Elements is:", total)

def ProElements(numbers):
    product = 1
    for num in numbers:
        product *= num
    print("Product of Elements is:", product)

def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))
    if len(Data) == 0:
        print("Please enter at least one number.")
        return

    print("User input list:", Data)

    t1 = threading.Thread(target=SumElements, args=(Data,))
    t2 = threading.Thread(target=ProElements, args=(Data,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()
