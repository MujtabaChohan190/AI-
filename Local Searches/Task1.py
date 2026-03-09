# TASK 1: BEAM SEARCH - FIND LOWEST COST PATH FROM A BACK TO A
# The task asks to find minimum cost path to come back home after visiting friends
# We'll find the lowest cost cycle from A back to A (not necessarily visiting ALL nodes)

# Graph from image
graph = {
    'A': [('E', 30), ('B', 7), ('C', 4)],
    'B': [('A', 7), ('C', 9), ('E', 3), ('D', 9)],
    'C': [('A', 4), ('B', 9), ('D', 8), ('E', 6), ('F', 5)],
    'D': [('B', 9), ('C', 8), ('E', 10)],
    'E': [('A', 30), ('B', 3), ('C', 6), ('D', 10)],
    'F': [('C', 5)]
}

def beam_search_paths(start, goal, beam_width=3, max_depth=10):
    """
    Beam Search to find paths from start to goal
    Returns multiple paths with their costs
    """
    beam = [(0, [start])]
    completed_paths = []
    
    for depth in range(max_depth):
        if not beam:
            break
        
        candidates = []
        
        for cost, path in beam:
            current = path[-1]
            
            # Check if we reached goal
            if current == goal and len(path) > 1:
                completed_paths.append((cost, path))
                continue
            
            # Prevent very long paths
            if len(path) >= max_depth:
                continue
            
            # Expand neighbors
            for neighbor, edge_cost in graph[current]:
                # Avoid immediate backtracking to previous node
                if len(path) > 1 and neighbor == path[-2]:
                    continue
                
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))
        
        if not candidates:
            break
        
        # Sort and keep best beam_width paths
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:beam_width]
    
    # Sort completed paths by cost
    completed_paths.sort(key=lambda x: x[0])
    return completed_paths

# Run Beam Search
print("="*70)
print("TASK 1: BEAM SEARCH - FIND MINIMUM COST CYCLE FROM A TO A")
print("="*70)

print("\nGraph Structure:")
print(f"{'Node':<8} {'Connections (neighbor, cost)'}")
print("-"*70)
for node in sorted(graph.keys()):
    connections = ', '.join([f"{n}({c})" for n, c in graph[node]])
    print(f"{node:<8} {connections}")

print("\n" + "="*70)
print("OBJECTIVE: Find lowest cost path from A back to A")
print("="*70)

# Find paths with different beam widths
print("\nSearching for paths from A to A...\n")

for beam_width in [3, 5, 10]:
    print(f"{'─'*70}")
    print(f"Beam Width = {beam_width}")
    print(f"{'─'*70}")
    
    paths = beam_search_paths('A', 'A', beam_width=beam_width, max_depth=8)
    
    if paths:
        # Show top 3 paths
        print(f"Found {len(paths)} paths. Top 3:")
        for i, (cost, path) in enumerate(paths[:3], 1):
            print(f"  {i}. {' → '.join(path):<40} Cost: {cost}")
    else:
        print("  No paths found")
    print()

print("="*70)
print("BEST SOLUTION:")
print("="*70)

# Get best path with large beam width
all_paths = beam_search_paths('A', 'A', beam_width=20, max_depth=8)

if all_paths:
    best_cost, best_path = all_paths[0]
    
    print(f"\nShortest Cycle: {' → '.join(best_path)}")
    print(f"Total Cost: {best_cost}")
    print(f"\nPath Breakdown:")
    
    cumulative = 0
    for i in range(len(best_path) - 1):
        from_node = best_path[i]
        to_node = best_path[i + 1]
        
        for neighbor, edge_cost in graph[from_node]:
            if neighbor == to_node:
                cumulative += edge_cost
                print(f"  Step {i+1}: {from_node} → {to_node}  (cost: {edge_cost}, cumulative: {cumulative})")
                break
    
    print(f"\n✓ This is the minimum cost cycle from A back to A")
else:
    print("No cycle found")
