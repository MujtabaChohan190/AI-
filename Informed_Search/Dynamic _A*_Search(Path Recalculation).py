# This program demonstrates Dynamic A* Search.
# A* is first used to find the shortest path in the maze.
# If an obstacle appears during navigation, the algorithm
# recalculates a new optimal path from the current position
# to the goal using the A* strategy.

import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def a_star(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        _, current = heapq.heappop(open_list)

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

                    heapq.heappush(open_list, (f_cost, next_node))
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
goal = (4,4)

path = a_star(maze, start, goal)

print("Initial Path:", path)

# Simulate obstacle appearing dynamically
maze[2][2] = 1

print("Obstacle added at (2,2). Recalculating path...")

path = a_star(maze, start, goal)

print("New Path:", path)
