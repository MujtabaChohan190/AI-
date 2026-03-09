# Maze (1 = open path, 0 = blocked)
#This program converts a maze into a graph and then runs BFS to reach the goal.
maze = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 1, 1]
]

# Possible movements (right, down)
directions = [(0,1),(1,0)]

# Convert maze into graph
def create_graph(maze):

    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):

            if maze[i][j] == 1:

                neighbors = []

                for dx,dy in directions:

                    nx = i + dx
                    ny = j + dy

                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbors.append((nx,ny))

                graph[(i,j)] = neighbors

    return graph


# BFS Function
def bfs(graph,start,goal):

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:

        node = queue.pop(0)
        print(node,end=" ")

        if node == goal:
            print("\nGoal Found")
            return

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


# Create graph from maze
graph = create_graph(maze)

start = (0,0)
goal = (2,2)

print("Maze BFS Traversal:")
bfs(graph,start,goal)
