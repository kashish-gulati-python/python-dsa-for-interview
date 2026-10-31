from multiprocessing import Process, current_process
from time import sleep, perf_counter

def count_number():
    count = 0
    print(f"{current_process().name} has started counting the number: count = {count}")
    for _ in range(100_000_000):
        count += 1
    print(f"{current_process().name} has started ended the number: count = {count}")

if __name__=='__main__':

    start_time = perf_counter()
    p1 = Process(target=count_number, name="counter-1")
    p2 = Process(target=count_number, name="counter-2")

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end_time = perf_counter()

    elapsed_time = end_time - start_time
    print(f"Program executed in {elapsed_time:.6f} seconds.")