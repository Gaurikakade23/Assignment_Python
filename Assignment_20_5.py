import threading

def print_ascending():
    print("Thread Name:", threading.current_thread().name)
    for i in range(1, 51):
        print(i, end=" ")
    print("\n")

def print_descending():
    print("Thread Name:", threading.current_thread().name)
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()

t1 = threading.Thread(target=print_ascending, name="Thread1")
t2 = threading.Thread(target=print_descending, name="Thread2")

t1.start()

t1.join()

t2.start()

t2.join()