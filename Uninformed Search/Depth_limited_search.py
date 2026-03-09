# Depth Limited Search

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

def dls(node, goal, depth):

    if depth == 0 and node == goal:
        print("Goal Found:", node)
        return True

    if depth > 0:
        for child in graph[node]:
            if dls(child, goal, depth - 1):
                print(node, end=" ")
                return True

    return False

start = 'A'
goal = 'I'
depth_limit = 3

print("DLS Search:")
dls(start, goal, depth_limit)
