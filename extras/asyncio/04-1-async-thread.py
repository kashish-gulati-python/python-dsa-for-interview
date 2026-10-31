import asyncio
from time import sleep, perf_counter

def check_stock(item):
    print(f"Checking {item}...")
    sleep(2)  # Simulated blocking delay
    return f"{item}: Available"

async def main():
    items = ["Masala Chai", "Green Chai", "Ginger Chai"]
    
    start_time = perf_counter()

    # Fire off all 3 blocking tasks at the EXACT SAME TIME
    tasks = [asyncio.to_thread(check_stock, item) for item in items]
    results = await asyncio.gather(*tasks)

    print(results)
    print(f"Total time: {perf_counter() - start_time:.2f} seconds")

asyncio.run(main())