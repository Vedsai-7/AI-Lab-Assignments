from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

bfs('A', 'F')