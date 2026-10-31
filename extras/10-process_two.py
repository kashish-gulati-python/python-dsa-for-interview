from multiprocessing import Process
from time import perf_counter

total = 0

def cpu_heavy():
    global total
    print("Counting some numbers...")
    for _ in range(10**7):
        total += 1
    print("Done ✅")

if __name__ == "__main__":
    start_time = perf_counter()

    processes = [Process(target=cpu_heavy) for _ in range(10)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    end_time = perf_counter()

    elapsed_time = end_time - start_time
    print(f"Total: {total}")
    print(f"Time taken: {elapsed_time:.4f} seconds.")