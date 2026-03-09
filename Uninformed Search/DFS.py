# Depth First Search

graph = {
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

def dfs(graph, start, goal):

    visited = []
    stack = []

    visited.append(start)
    stack.append(start)

    while stack:

        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            return

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

start = 'A'
goal = 'I'

print("DFS Traversal:")
dfs(graph, start, goal)
