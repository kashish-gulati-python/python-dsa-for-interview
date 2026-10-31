from multiprocessing import Process, cpu_count
from time import perf_counter

def count_range(start, end):
    total = 0
    for _ in range(start, end):
        total += 1

if __name__ == '__main__':
    TOTAL_COUNT = 100_000_000
    num_cores = cpu_count()
    chunk_size = TOTAL_COUNT // num_cores
    
    processes = []
    start_time = perf_counter()

    for i in range(num_cores):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1 if i != num_cores - 1 else TOTAL_COUNT + 1
        
        p = Process(target=count_range, args=(start, end))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Multiprocessing ({num_cores} cores) took: {perf_counter() - start_time:.2f}s")