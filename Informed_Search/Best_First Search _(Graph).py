# This program implements Best-First Search on a graph.
# It uses a Priority Queue and a heuristic value to decide
# which node to visit next. The node with the lowest heuristic
# value is expanded first until the goal node is found.

from queue import PriorityQueue

graph = {
    'S': [('A',3), ('B',6), ('C',5)],
    'A': [('D',9), ('E',8)],
    'B': [('F',12), ('G',14)],
    'C': [('H',7)],
    'H': [('I',5), ('J',6)],
    'I': [('K',1), ('L',10), ('M',2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [],
    'L': [], 'M': []
}

def best_first_search(graph, start, goal):

    visited = set()
    pq = PriorityQueue()

    pq.put((0,start)) //A → PQ: [(9,D), (8,E)]
    while not pq.empty():
        cost,node = pq.get() //gets smallest node 
        if node not in visited:
            print(node,end=" ")
            visited.add(node) //we add all nodes in visited 

            if node == goal:
                print("\nGoal Reached")
                return
                
//Expanding node 
            for neighbor,weight in graph[node]: //unpack tuple - A -> (d , 10) 
                if neighbor not in visited:
                    pq.put((weight,neighbor))

print("Best First Search:")
best_first_search(graph,'A','I')
