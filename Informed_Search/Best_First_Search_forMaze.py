# This program solves a maze using Best-First Search.
# It uses the Manhattan Distance heuristic to guide
# the search towards the goal. The algorithm expands
# the node with the lowest heuristic value first and
# reconstructs the path once the goal is reached.

from queue import PriorityQueue

# 🔹 Heuristic (single goal version)
def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def best_first_search(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    frontier = PriorityQueue()
    frontier.put((0, start))   # (priority, position)

    visited = set()
    parent = {start: None}

    while not frontier.empty():

        _, current = frontier.get()

        # 🔹 Goal check
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        visited.add(current)

        x, y = current

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

            nx = x + dx
            ny = y + dy
            next_pos = (nx, ny)

            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] == 0 and
                next_pos not in visited):

                parent[next_pos] = current

                # 🔹 priority = heuristic
                h = heuristic(next_pos, goal)

                frontier.put((h, next_pos))
                visited.add(next_pos)

    return None


# 🔹 TEST (your original maze)
maze = [
[0,0,1,0,0],
[0,0,0,0,0],
[0,0,1,0,1],
[0,0,1,0,0],
[0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

path = best_first_search(maze, start, goal)

print("Path:", path)




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
