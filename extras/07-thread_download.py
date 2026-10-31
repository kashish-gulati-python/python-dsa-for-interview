import threading
import requests
from time import time, perf_counter
from pathlib import Path

def download_and_save(url, filename):
    print(f"Started downloading image from url: {url}...")
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Finished downloading and saved as '{filename}' ({len(response.content)} bytes)")
    else:
        print(f"Failed to download {url} - Status Code: {response.status_code}")

    print(f"Finished downloading image from url: {url} with size: {len(response.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start_time = perf_counter()
threads = []

for i, url in enumerate(urls, start=1):
    ext = url.split('/')[-1]
    # Line of code to resolve the script's directory dynamically
    filename = Path(__file__).parent / f"image_{i}.{ext}"
    # # Line of code to specify the hardcoded path
    # filename = os.path.join("extras", f"downloaded_image_{i}.{ext}")
    t = threading.Thread(target=download_and_save, args=(url, filename))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end_time = perf_counter()

elapsed_time = end_time - start_time
print(f"All images downloaded in {elapsed_time:.4f} seconds.")