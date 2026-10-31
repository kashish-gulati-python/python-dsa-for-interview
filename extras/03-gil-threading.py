import threading
from time import sleep, perf_counter

def count_number():
    count = 0
    print(f"{threading.current_thread().name} has started counting the number: count = {count}")
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} has started ended the number: count = {count}")

start_time = perf_counter()

thread1 = threading.Thread(target=count_number, name="counter-1")
thread2 = threading.Thread(target=count_number, name="counter-2")

thread1.start()
thread2.start()
thread1.join()
thread2.join()

end_time = perf_counter()

elapsed_time = end_time - start_time
print(f"Program executed in {elapsed_time:.6f} seconds.")