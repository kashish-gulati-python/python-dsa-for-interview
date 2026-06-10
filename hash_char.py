s = "abdnssovadab"
q = ["d", "a", "v", "s", "e"]

for i in q:
    count = 0
    for j in s:
        if i == j:
            count += 1
    print(f"{i}:", count)