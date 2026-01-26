import threading

counter = 0
lock = threading.Lock()

def increment_counter(times):
    global counter
    for i in range(times):
        lock.acquire()
        counter += 1
        lock.release()   # <-- fix here

num_threads = 5
increments_per_thread = 1000

threads = []

for i in range(num_threads):
    t = threading.Thread(target=increment_counter, args=(increments_per_thread,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final value of counter:", counter)
