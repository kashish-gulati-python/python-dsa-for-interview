import threading
from time import sleep, perf_counter

def make_chai(type_, wait_time):
    print(f"{type_} chai: Brewing...")
    sleep(wait_time)
    print(f"{type_} chai: Ready...")

start_time = perf_counter()

t1 = threading.Thread(target=make_chai, args=("Masala", 2))
t2 = threading.Thread(target=make_chai, args=("Ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

elapsed_time = end_time - start_time
print(f"Breakfast is ready in {elapsed_time:.4f} seconds.")