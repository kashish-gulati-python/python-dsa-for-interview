from multiprocessing import Process
from time import sleep, perf_counter


def brew_chai(name):
    print(f"Start brewing {name}'s chai")
    sleep(3)
    print(f"End brewing {name}'s chai")


if __name__ == '__main__': # Ensures process spawning only happens in the main script (critical for multiprocessing to avoid recursive loop crashes).

    start_time = perf_counter()
    # Process workers, each assigned to run brew_chai("Chai maker #1"), #2, and #3.
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{i}", ))
        for i in range(1, 4)
    ]

    # Kicks off all 3 process workers almost simultaneously.
    for p in chai_makers:
        p.start()

    # Tells your main program, "Wait right here until both threads complete before moving on."
    for p in chai_makers:
        p.join()

    end_time = perf_counter()

    elapsed_time = end_time - start_time
    print(f"Program executed in {elapsed_time:.6f} seconds.")