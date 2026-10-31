import asyncio
import threading
from time import sleep

def background_worker():
    while True:
        sleep(1)
        print("Logging system health 🍎")

async def main():
    await asyncio.sleep(3)
    print("Order fetched!!")

threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(main())