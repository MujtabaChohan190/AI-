# TASK 2: HILL CLIMBING - 8-PUZZLE PROBLEM
# Arrange tiles from random initial state to goal state using Hill Climbing

import random
import copy

# Goal state configuration
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents empty space
]

def create_random_initial_state():
    """
    Create a random initial state by shuffling numbers 0-8
    """
    numbers = list(range(9))
    random.shuffle(numbers)
    
    state = []
    for i in range(3):
        row = numbers[i*3:(i+1)*3]
        state.append(row)
    
    return state

def find_blank(state):
    """
    Find position of blank tile (0)
    Returns: (row, col)
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def calculate_heuristic(state):
    """
    Heuristic: Number of misplaced tiles
    Lower is better (0 = goal state)
    """
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced

def get_neighbors(state):
    """
    Generate all possible next states by moving blank tile
    Can move: Up, Down, Left, Right
    """
    neighbors = []
    blank_row, blank_col = find_blank(state)
    
    # Possible moves: (row_change, col_change)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dr, dc in moves:
        new_row = blank_row + dr
        new_col = blank_col + dc
        
        # Check if move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Create new state
            new_state = copy.deepcopy(state)
            
            # Swap blank with adjacent tile
            new_state[blank_row][blank_col] = new_state[new_row][new_col]
            new_state[new_row][new_col] = 0
            
            neighbors.append(new_state)
    
    return neighbors

def hill_climbing(initial_state, max_iterations=1000):
    """
    Hill Climbing algorithm for 8-puzzle
    
    Returns: Final state, number of moves, success status
    """
    current = initial_state
    current_h = calculate_heuristic(current)
    
    moves = 0
    
    for iteration in range(max_iterations):
        # Check if goal reached
        if current_h == 0:
            return current, moves, True
        
        # Get all neighbors
        neighbors = get_neighbors(current)
        
        # Find best neighbor
        best_neighbor = None
        best_h = current_h
        
        for neighbor in neighbors:
            h = calculate_heuristic(neighbor)
            if h < best_h:
                best_h = h
                best_neighbor = neighbor
        
        # If no better neighbor, stuck in local minimum
        if best_neighbor is None:
            return current, moves, False
        
        # Move to best neighbor
        current = best_neighbor
        current_h = best_h
        moves += 1
    
    return current, moves, False

def print_state(state, title="State"):
    """
    Print puzzle state in readable format
    """
    print(f"\n{title}:")
    print("-" * 13)
    for row in state:
        print("|", end="")
        for val in row:
            if val == 0:
                print("   |", end="")
            else:
                print(f" {val} |", end="")
        print()
        print("-" * 13)

def is_solvable(state):
    """
    Check if puzzle is solvable
    Count inversions - if even, solvable; if odd, not solvable
    """
    flat = []
    for row in state:
        for val in row:
            if val != 0:
                flat.append(val)
    
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    
    return inversions % 2 == 0

# Run Hill Climbing
print("="*60)
print("TASK 2: HILL CLIMBING - 8-PUZZLE PROBLEM")
print("="*60)

print_state(GOAL_STATE, "Goal State")

print("\n" + "="*60)
print("ATTEMPTING TO SOLVE RANDOM PUZZLES")
print("="*60)

max_attempts = 10
solved = False

for attempt in range(1, max_attempts + 1):
    print(f"\n{'='*60}")
    print(f"ATTEMPT {attempt}")
    print("="*60)
    
    # Create random initial state
    initial = create_random_initial_state()
    
    # Check if solvable
    if not is_solvable(initial):
        print("❌ Puzzle not solvable (odd number of inversions)")
        print_state(initial, "Initial State")
        continue
    
    print("✓ Puzzle is solvable")
    print_state(initial, "Initial State")
    
    initial_h = calculate_heuristic(initial)
    print(f"\nInitial heuristic (misplaced tiles): {initial_h}")
    
    # Run Hill Climbing
    final, moves, success = hill_climbing(initial)
    
    if success:
        print(f"\n✓✓✓ SUCCESS! Solved in {moves} moves ✓✓✓")
        print_state(final, "Final State")
        solved = True
        break
    else:
        final_h = calculate_heuristic(final)
        print(f"\n❌ Stuck in local minimum after {moves} moves")
        print(f"Final heuristic: {final_h}")
        print_state(final, "Final State (Stuck)")

if not solved:
    print(f"\n{'='*60}")
    print(f"Could not solve in {max_attempts} attempts")
    print("Hill Climbing often gets stuck in local minima for 8-puzzle")
    print("Consider using A* or other algorithms for better results")
    print("="*60)
