# BEAM SEARCH ALGORITHM
# This code implements Beam Search for finding the shortest path in a graph


graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 10), ('L', 2)],
    'D': [], 'E': [], 'F': [], 'G': [], 'J': [], 'K': [], 'L': []
}

def beam_search(start, goal, beam_width=2):
    beam = [(0, [start])]
    
    while beam:
        candidates = []
        
        for cost, path in beam:
            current = path[-1]
            
            if current == goal:
                return path, cost
            
            for neighbor, edge_cost in graph.get(current, []):
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))
        
        if not candidates:
            return None, float('inf')
        
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:beam_width]
    
    return None, float('inf')

# Run the code
start_node = 'S'
goal_node = 'L'
beam_width = 2

print(f"Beam Search from {start_node} to {goal_node}")
print(f"Beam Width: {beam_width}\n")

path, cost = beam_search(start_node, goal_node, beam_width)

if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found!")
