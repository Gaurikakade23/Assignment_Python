import threading
def even_list(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", evens)
    print("Sum of even numbers:", sum(evens))


def odd_list(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    print("Odd numbers:", odds)
    print("Sum of odd numbers:", sum(odds))


if __name__ == "__main__":
    num_list = [10, 15, 20, 25, 30, 35, 40]

    t1 = threading.Thread(target=even_list, args=(num_list,), name="EvenList")
    t2 = threading.Thread(target=odd_list, args=(num_list,), name="OddList")

    t1.start()
    t2.start()



