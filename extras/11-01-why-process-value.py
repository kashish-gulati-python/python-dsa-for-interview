from multiprocessing import Process, Queue

def worker(task_queue, result_queue):
    while not task_queue.empty():
        number = task_queue.get()
        result = number * number  # Do work
        result_queue.put(f"Square of {number} is {result}")

if __name__ == '__main__':
    tasks = Queue()
    results = Queue()

    # Add 5 numbers to the task queue
    for i in range(1, 6):
        tasks.put(i)

    # Launch 2 worker processes
    workers = [Process(target=worker, args=(tasks, results)) for _ in range(2)]
    
    for w in workers: w.start()
    for w in workers: w.join()

    # Collect and print all results
    while not results.empty():
        print(results.get())