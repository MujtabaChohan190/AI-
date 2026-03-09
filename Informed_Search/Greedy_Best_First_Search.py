# This program implements Greedy Best-First Search.
# The algorithm expands the node that appears closest
# to the goal based only on the heuristic value h(n).
# It ignores the path cost g(n), which makes it faster
# but not always optimal.

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


def greedy_bfs(graph,start,goal):

    frontier=[(start,heuristic[start])]
    visited=set()
    came_from={start:None}

    while frontier:

        frontier.sort(key=lambda x:x[1])

        current_node,_=frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node,end=" ")
        visited.add(current_node)

        if current_node==goal:

            path=[]

            while current_node is not None:
                path.append(current_node)
                current_node=came_from[current_node]

            path.reverse()

            print("\nGoal found with GBFS. Path:",path)
            return

        for neighbor in graph[current_node]:

            if neighbor not in visited:
                came_from[neighbor]=current_node
                frontier.append((neighbor,heuristic[neighbor]))

    print("\nGoal not found")


print("\nFollowing is the Greedy Best-First Search:")
greedy_bfs(graph,'A','I')
