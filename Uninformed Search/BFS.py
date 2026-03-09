# Breadth First Search

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

def bfs(graph, start, goal):

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:

        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start = 'A'
goal = 'I'

print("BFS Traversal:")
bfs(tree, start, goal)
