# This program implements the A* Search Algorithm.
# A* combines the path cost g(n) and heuristic h(n)
# to calculate f(n) = g(n) + h(n).
# It always expands the node with the lowest f(n),
# making it both complete and optimal when the
# heuristic is admissible.

graph = {
'A': {'B':4,'C':3},
'B': {'E':12,'F':5},
'C': {'D':7,'E':10},
'D': {'E':2},
'E': {'G':5},
'F': {'G':16},
'G': {}
}

heuristic = {
'A':14,'B':12,'C':11,'D':6,'E':4,'F':11,'G':0
}


def a_star(graph,start,goal):

    frontier=[(start,heuristic[start])]
    visited=set()

    g_costs={start:0}

    came_from={start:None}

    while frontier:

        frontier.sort(key=lambda x:x[1])

        current_node,current_f=frontier.pop(0)

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

            print("\nGoal found with A*. Path:",path)
            return

        for neighbor,cost in graph[current_node].items():

            new_g_cost=g_costs[current_node]+cost
            f_cost=new_g_cost+heuristic[neighbor]

            if neighbor not in g_costs or new_g_cost<g_costs[neighbor]:

                g_costs[neighbor]=new_g_cost
                came_from[neighbor]=current_node
                frontier.append((neighbor,f_cost))

    print("\nGoal not found")


print("\nFollowing is the A* Search:")
a_star(graph,'A','G')
