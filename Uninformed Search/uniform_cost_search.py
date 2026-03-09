# Uniform Cost Search

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

def ucs(graph, start, goal):

    frontier = [(start, 0)]
    visited = set()
    parent = {start: None}

    while frontier:

        frontier.sort(key=lambda x: x[1])
        node, cost = frontier.pop(0)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:

            path = []
            while node:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("Path:", path)
            print("Total Cost:", cost)
            return

        for neighbour, weight in graph[node].items():

            if neighbour not in visited:
                parent[neighbour] = node
                frontier.append((neighbour, cost + weight))

ucs(graph, 'A', 'I')
