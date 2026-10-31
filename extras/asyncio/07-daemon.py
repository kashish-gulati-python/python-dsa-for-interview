"""
When should you use Daemon Threads?
Use daemon=True for: Logging services, heartbeats, periodic status checks, file auto-savers,
garbage collection monitoring—tasks where it is safe to kill them abruptly when the main application stops.

Avoid daemon=True for: Financial transactions, writing critical files to disk, network requests that must complete,
or database writes. Abruptly killing a daemon thread mid-write can corrupt data!
"""

import threading
from time import sleep

def monitor_temperature():
    while True:
        print("Monitoring temperature...")
        sleep(3)

threading.Thread(target=monitor_temperature, daemon=True).start()
# threading.Thread(target=monitor_temperature).start() # default: daemon=False

print("Main program executed")