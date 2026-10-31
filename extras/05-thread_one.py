import threading
from time import sleep, perf_counter

def boil_milk():
    print("Boiling Milk...")
    sleep(2)
    print("Milk boiled.")

def toast_bun():
    print("Toasting Bun...")
    sleep(3)
    print("Bun Toasted.")

start_time = perf_counter()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

elapsed_time = end_time - start_time
print(f"Breakfast is ready in {elapsed_time:.4f} seconds.")