from queue import PriorityQueue

# Define the Node class for consistent structure
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.h = 0  # Heuristic (Manhattan distance)
        self.f = 0  # Priority (In Best-First, f = h)

    def __lt__(self, other):
        # This allows PriorityQueue to sort Nodes by their f-score
        return self.f < other.f

def heuristic_multi(current_pos, goals):
    # Manhattan distance to the CLOSEST goal in the list
    return min(abs(current_pos[0] - g[0]) + abs(current_pos[1] - g[1]) for g in goals)

def best_first_multi_goal(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    
    # Initialize start node
    start_node = Node(start)
    start_node.h = heuristic_multi(start, goals)
    start_node.f = start_node.h

    frontier = PriorityQueue()
    frontier.put(start_node)
    
    visited = set()

    while not frontier.empty():
        # Pop the node with the lowest f (heuristic)
        current_node = frontier.get()
        current_pos = current_node.position

        # GOAL CHECK: Is this position one of our goals?
        if current_pos in goals:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] # Reverse path

        visited.add(current_pos)

        # EXPAND: Check neighbors
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)

            # Boundary and obstacle checks
            if (0 <= new_pos[0] < rows and 
                0 <= new_pos[1] < cols and 
                maze[new_pos[0]][new_pos[1]] == 0 and 
                new_pos not in visited):

                new_node = Node(new_pos, current_node)
                # In Best-First Search, we only care about the heuristic
                new_node.h = heuristic_multi(new_pos, goals)
                new_node.f = new_node.h

                frontier.put(new_node)
                visited.add(new_pos)

    return None

# --- Setup and Execution ---
maze = [
    [0,0,0,1,0],
    [1,0,0,1,0],
    [0,0,0,0,0],
    [0,1,1,0,1],
    [0,0,0,0,0]
]

start = (0,0)
goals = [(4,4), (2,4)]

path = best_first_multi_goal(maze, start, goals)

if path:
    print(f"Path to nearest goal {path[-1]}:", path)
else:
    print("No path found to any goal.")
