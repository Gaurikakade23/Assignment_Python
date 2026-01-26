import threading
def count_small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase count:", count)
    print()

def count_capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase count:", count)
    print()

def count_digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits count:", count)
    print()

string = input("Enter a string: ")

t1 = threading.Thread(target=count_small, args=(string,), name="Small")
t2 = threading.Thread(target=count_capital, args=(string,), name="Capital")
t3 = threading.Thread(target=count_digits, args=(string,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()