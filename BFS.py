from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(start):
    queue = deque()

    visited = set()

    queue.append(start)

    visited.add(start)

    print("BFS Traversal:")

    while queue:

        current = queue.popleft()

        print(current, end=" ")

        for neighbor in graph[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)


bfs('A')