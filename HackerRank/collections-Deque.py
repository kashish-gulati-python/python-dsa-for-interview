from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    method_value = input().split()
    method = method_value[0]
    if len(method_value) > 1:
        value = method_value[-1]
        eval(f"d.{method}({value})")
    else:
        eval(f"d.{method}()")

print(*list(d))

"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints
0 < N <= 100

Output Format

Print the space separated elements of deque d.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2
"""