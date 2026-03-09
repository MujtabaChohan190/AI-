from collections import deque

maze = [
    [1,1,0],
    [1,1,0],
    [0,1,1]
]

rows = len(maze)
cols = len(maze[0])

directions = [(0,1),(1,0)]

def bfs(start,goal):

    queue = deque()
    queue.append((start,[start]))

    visited=set()

    while queue:

        (x,y),path = queue.popleft()

        if (x,y) == goal:
            print("Path to goal:",path)
            return

        visited.add((x,y))

        for dx,dy in directions:

            nx = x + dx
            ny = y + dy

            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==1 and (nx,ny) not in visited:
                queue.append(((nx,ny),path+[(nx,ny)]))


start=(0,0)
goal=(2,2)

bfs(start,goal)
