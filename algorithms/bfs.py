from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def bfs(graph, start):
    queue = deque(start)
    visited = set()
    print(queue)

    while queue:
        node = queue.popleft()
        print(queue)

        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

bfs(graph, "A")

r"""
      A
     / \
    B   C
   / \   \
  D   E   F
BFS explores level by level.

Starting from A, it visits:

A
↓
B C
↓
D E F

Traversal order:

A → B → C → D → E → F
Rule

Always visit all neighbors before going deeper.

Because of this, BFS uses a Queue (FIFO).

"""