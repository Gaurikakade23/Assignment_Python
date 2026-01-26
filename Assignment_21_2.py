import threading

def Maximum(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    print("Maximum Element is:", max_val)

def Minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    print("Minimum Element is:", min_val)

def main():
    Data = list(map(int, input("Enter numbers separated by space: ").split()))
    if len(Data) == 0:
        print("Please enter at least one number.")
        return

    print("User input list:", Data)

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()
