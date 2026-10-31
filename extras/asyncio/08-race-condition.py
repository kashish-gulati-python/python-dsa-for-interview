import threading

stock = 0

def restock():
    global stock
    for _ in range(100_000):
        stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

# for t in threads: t.start() # same as above
# for t in threads: t.join()

print(f"Chai Stock: {stock}")