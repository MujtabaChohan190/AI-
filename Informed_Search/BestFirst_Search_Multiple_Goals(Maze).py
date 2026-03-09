# This program applies Best-First Search to a maze that contains
# multiple possible goal positions. The algorithm uses the
# Manhattan Distance heuristic to guide the search toward the
# closest goal. It explores the maze using a priority queue and
# returns the path to whichever goal is reached first.

from queue import PriorityQueue

def heuristic(pos, goals):
    # return minimum Manhattan distance to any goal
    return min(abs(pos[0]-g[0]) + abs(pos[1]-g[1]) for g in goals)


def best_first_multi_goal(maze, start, goals):

    rows = len(maze)
    cols = len(maze[0])

    frontier = PriorityQueue()
    frontier.put((0, start))

    visited = set()
    parent = {start: None}

    while not frontier.empty():

        _, current = frontier.get()

        if current in goals:

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
                frontier.put((heuristic(next_pos, goals), next_pos))
                visited.add(next_pos)

    return None


maze = [
[0,0,0,1,0],
[1,0,0,1,0],
[0,0,0,0,0],
[0,1,1,0,1],
[0,0,0,0,0]
]

start = (0,0)

goals = [(4,4),(2,4)]

path = best_first_multi_goal(maze, start, goals)

print("Path to nearest goal:", path)
