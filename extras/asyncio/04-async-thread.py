import asyncio
from time import sleep
# from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in the stock...")
    sleep(2)
    return f"{item} is available. Qty: 39"

async def main():
    # loop = asyncio.get_running_loop()
    # with ThreadPoolExecutor() as pool:
        # result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
    result = await asyncio.to_thread(check_stock, "Masala Chai") # Modern alternative (Python 3.9+)
    print(result)

asyncio.run(main())