# This program solves a maze using Best-First Search.
# It uses the Manhattan Distance heuristic to guide
# the search towards the goal. The algorithm expands
# the node with the lowest heuristic value first and
# reconstructs the path once the goal is reached.



from queue import PriorityQueue

class Node:

    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(current_pos, end_pos):
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])


def best_first_search(maze, start, end):

    rows, cols = len(maze), len(maze[0])

    start_node = Node(start)
    end_node = Node(end)

    frontier = PriorityQueue()
    frontier.put(start_node)

    visited = set()

    while not frontier.empty():

        current_node = frontier.get()
        current_pos = current_node.position

        if current_pos == end:

            path = []

            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent

            return path[::-1]

        visited.add(current_pos)

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

            new_pos = (current_pos[0] + dx, current_pos[1] + dy)

            if (0 <= new_pos[0] < rows and
                0 <= new_pos[1] < cols and
                maze[new_pos[0]][new_pos[1]] == 0 and
                new_pos not in visited):

                new_node = Node(new_pos, current_node)

                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, end)

                new_node.f = new_node.h

                frontier.put(new_node)
                visited.add(new_pos)

    return None


maze = [
[0,0,1,0,0],
[0,0,0,0,0],
[0,0,1,0,1],
[0,0,1,0,0],
[0,0,0,1,0]
]

start = (0,0)
end = (4,4)

path = best_first_search(maze,start,end)

if path:
    print("Path found:", path)
else:
    print("No path found")




# ============================================================
# MAZE BEST FIRST SEARCH — HOW IT WORKS
# ============================================================

# STEP 1 — SETUP
# Create start Node at (0,0) and put it into the frontier PQ
# frontier = [Node(pos=(0,0), f=0)]

# STEP 2 — LOOP (repeat until frontier is empty)
# Pop the node with the lowest f (= heuristic h) score
# Example: frontier had [Node(f=2), Node(f=5)] → pop Node(f=2)

# STEP 3 — GOAL CHECK
# If current position == end position → trace parents back
# Build path by following .parent links → reverse → return path
# Example: (4,4)→(3,4)→(2,4)→...→(0,0) reversed = full path ✅

# STEP 4 — EXPAND (only if not goal)
# Try all 4 directions: Down(1,0) Up(-1,0) Right(0,1) Left(0,-1)
# For each neighbor → check bounds + not wall + not visited
# Calculate h = Manhattan Distance to goal
# Set f = h → push new Node into frontier

# STEP 5 — REPEAT
# Go back to STEP 2 and pop next lowest f node
# Keep going until goal found or frontier becomes empty
