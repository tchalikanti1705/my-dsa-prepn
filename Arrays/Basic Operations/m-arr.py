from collections import deque

def bfs(tree, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

print("BFS Traversal:")
bfs(tree, 1)
