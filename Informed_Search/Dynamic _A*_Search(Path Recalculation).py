# This program demonstrates Dynamic A* Search.
# A* is first used to find the shortest path in the maze.
# If an obstacle appears during navigation, the algorithm
# recalculates a new optimal path from the current position
# to the goal using the A* strategy.

from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])
    
    open_list = PriorityQueue()
    open_list.put((0, start))
    
    g_cost = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        x, y = current
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + dx
            ny = y + dy
            next_node = (nx, ny)
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 1:
                    continue
                new_g = g_cost[current] + 1
                if next_node not in g_cost or new_g < g_cost[next_node]:
                    g_cost[next_node] = new_g
                    f_cost = new_g + heuristic(next_node, goal)
                    open_list.put((f_cost, next_node))
                    parent[next_node] = current

    return None

maze = [
[0,0,0,0,0],
[0,1,1,1,0],
[0,0,0,1,0],
[1,1,0,0,0],
[0,0,0,1,0]
]
start = (0,0)
goal  = (4,4)

path = a_star(maze, start, goal)
print("Initial Path:", path)

maze[2][2] = 1
print("Obstacle added at (2,2). Recalculating...")

path = a_star(maze, start, goal)
print("New Path:", path)



# ============================================================
# DYNAMIC A* SEARCH — HOW IT WORKS
# ============================================================

# STEP 1 — SETUP
# Push start (0,0) into open_list with f=0
# g_cost = {(0,0): 0}   parent = {(0,0): None}

# STEP 2 — LOOP (repeat until open_list empty)
# open_list.get() pops cell with lowest f automatically
# Example: [(6,(2,0)),(7,(1,0))] → pop (6,(2,0))

# STEP 3 — GOAL CHECK
# If current == (4,4) → trace parent{} back to start
# Reverse → return complete path ✅

# STEP 4 — EXPAND
# Try 4 directions → check bounds → skip walls (==1)
# new_g = g_cost[current] + 1  (every step costs 1)
# f = new_g + manhattan distance to goal
# Only push if cheaper than known g_cost

# STEP 5 — OBSTACLE APPEARS
# maze[2][2] = 1  ← block a cell dynamically
# Run A* again on updated maze → finds new path
