graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}

V = 5
adj = {[] for _ in range(V)}
print(adj)

"""
Find the size of every connected component using DFS, then return the maximum size.

Example

Suppose we have this graph:

      0 ----- 1
      |       |
      |       |
      2

      3 ----- 4

      5

There are 3 trees (connected components):

Tree 1 : {0,1,2}    Size = 3
Tree 2 : {3,4}      Size = 2
Tree 3 : {5}        Size = 1

Answer:

Largest tree = 3
"""