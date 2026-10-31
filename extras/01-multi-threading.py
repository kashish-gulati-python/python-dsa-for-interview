import threading
from time import sleep

def take_orders():
    for i in range(1,4):
        print(f"Taking order #{i}")
        sleep(2)

def make_food():
    for i in range(1,4):
        print(f"Making food for order #{i}")
        sleep(3)


# Sets up two separate workers (threads) — one assigned to take_orders and one assigned to make_food.
order_thread = threading.Thread(target=take_orders)
make_thread = threading.Thread(target=make_food)


# Kicks off both workers. Python immediately hands control to both tasks so they run in parallel alongside each other.
order_thread.start()
make_thread.start()


# Tells your main program, "Wait right here until both threads complete before moving on."
# This ensures the final print("All orders taken and made in kitchen!") line only executes after all 3 orders are taken and cooked.
order_thread.join()
make_thread.join()

print("All orders taken and made in kitchen!")