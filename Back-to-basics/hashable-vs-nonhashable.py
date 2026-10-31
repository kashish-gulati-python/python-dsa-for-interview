buckets = [[] for _ in range(5)]

print(buckets)

def put(key, value):
    bucket_index = hash(key) % len(buckets)
    print(f"'{key}' goes to Bucket {bucket_index}")

    buckets[bucket_index].append((key, value))

def get(key):
    bucket_index = hash(key) % len(buckets)

    print(f"Looking in Bucket {bucket_index}")

    for stored_key, stored_value in buckets[bucket_index]:
        if stored_key == key:
            return stored_value

    raise KeyError(key)

put("apple", 10)
put("banana", 20)
put("cat", 30)

print(buckets)

print(get("banana"))