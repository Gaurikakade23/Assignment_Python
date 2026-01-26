import threading
import time

def print_even():
    for i in range(1, 11):
        print(f"Even: {i*2}")
        time.sleep(0.1)
    print("Even thread over")

def print_odd():
    for i in range(1, 11):
        print(f"Odd: {i*2 - 1}")
        time.sleep(0.1)
    print("Odd thread over")

even_thread = threading.Thread(target=print_even, args=())
odd_thread = threading.Thread(target=print_odd, args=())

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
