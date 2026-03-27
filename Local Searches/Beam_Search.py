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
  #if there is no expanded nodes from current node ie candidates       
        if not candidates:
            return None, float('inf')
  #there are candidates so sort it       
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





# ============================================================
# BEAM SEARCH — HOW IT WORKS
# ============================================================

# STEP 1 — SETUP
# beam = [(0, ['S'])]  ← one path, just start node, cost 0
# beam_width = 2       ← only keep top 2 paths at each level

# STEP 2 — LOOP (repeat while beam has paths)
# For every path in beam → get last node (current position)
# Expand current → build new paths by appending neighbors
# Collect all into candidates list

# STEP 3 — GOAL CHECK
# If last node of any path == goal → return that path ✅

# STEP 4 — PRUNE (heart of beam search)
# Sort candidates by cost
# Keep only top beam_width paths → discard rest ❌
# beam = candidates[:beam_width]

# STEP 5 — REPEAT
# New beam has only top k paths
# Keep expanding until goal found or beam empt
