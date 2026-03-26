from queue import PriorityQueue

graph = {
    'A': {'B':2,'C':1},
    'B': {'D':4,'E':3},
    'C': {'F':1,'G':5},
    'D': {'H':2},
    'E': {},
    'F': {'I':6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic = {
    'A':7,'B':6,'C':5,'D':4,'E':7,
    'F':3,'G':6,'H':2,'I':0
}

def greedy_bfs(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))
    visited = set()
    came_from = {start: None}

    while not frontier.empty():
        h, current_node = frontier.get()

        if current_node not in visited:          # ✅ simple check
            print(current_node, end=" ")
            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print("\nGoal found. Path:", path)
                return

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    came_from[neighbor] = current_node
                    frontier.put((heuristic[neighbor], neighbor))

    print("\nGoal not found")

greedy_bfs(graph, 'A', 'I')
