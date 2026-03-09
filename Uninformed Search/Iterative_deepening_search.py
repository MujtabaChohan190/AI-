# Iterative Deepening DFS

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

def dls(node, goal, depth, path):

    if depth == 0 and node == goal:
        path.append(node)
        return True

    if depth > 0:
        for child in tree[node]:
            if dls(child, goal, depth-1, path):
                path.append(node)
                return True

    return False

def iterative_deepening(start, goal, max_depth):

    for depth in range(max_depth + 1):

        path = []

        if dls(start, goal, depth, path):
            print("Path:", " -> ".join(reversed(path)))
            return

    print("Goal Not Found")

start = 'A'
goal = 'I'

iterative_deepening(start, goal, 5)
