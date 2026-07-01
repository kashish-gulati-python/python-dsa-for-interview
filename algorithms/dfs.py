graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node)
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

dfs(graph, "A")

r"""
      A
     / \
    B   C
   / \   \
  D   E   F
DFS goes as deep as possible before coming back.

Starting from A:

A
↓
B
↓
D
↑
B
↓
E
↑
A
↓
C
↓
F

Traversal

A → B → D → E → C → F

Notice how it finishes the entire left branch before moving right.

DFS uses a Stack (LIFO).

Last item inserted is removed first.
"""