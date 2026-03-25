# This program implements Best-First Search on a graph.
# It uses a Priority Queue and a heuristic value to decide
# which node to visit next. The node with the lowest heuristic
# value is expanded first until the goal node is found.


# STEP 1 — SETUP
# Put the starting node into the Priority Queue with cost 0
# pq = [(0, 'S')]

# STEP 2 — LOOP (repeat until PQ is empty)
# Pop the smallest/most promising node from PQ
# Example: pq had [(3,A),(5,C),(6,B)] → pop (3,A) first

# STEP 3 — GOAL CHECK
# If popped node == goal → print "Goal Reached" and STOP
# Example: node = 'K' and goal = 'K' → stop ✅

# STEP 4 — EXPAND (only if not goal)
# Loop through all neighbors of current node
# If neighbor not visited → push (weight, neighbor) into PQ
# Example: node='H' → push (5,I) and (6,J) into PQ

# STEP 5 — REPEAT
# Go back to STEP 2 and pop next smallest node
# Keep going until goal is found or PQ becomes empty


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

    pq.put((0,start))  #A → PQ: [(9,D), (8,E)]
    while not pq.empty():
        cost,node = pq.get() #gets smallest node 
        if node not in visited:
            print(node,end=" ")
            visited.add(node) //we add all nodes in visited 

            if node == goal:
                print("\nGoal Reached")
                return
                
#Expanding node 
            for neighbor,weight in graph[node]: #unpack tuple - A -> (d , 10) 
                if neighbor not in visited:
                    pq.put((weight,neighbor))

print("Best First Search:")
best_first_search(graph,'A','I')
