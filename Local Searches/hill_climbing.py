# HILL CLIMBING ALGORITHM - N-QUEENS PROBLEM
# This code solves the N-Queens problem using Hill Climbing

import random

def create_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def calculate_attacks(board):
    n = len(board)
    attacks = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    
    return attacks

def get_neighbors(board):
    n = len(board)
    neighbors = []
    
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                neighbor = board.copy()
                neighbor[col] = row
                neighbors.append((neighbor, calculate_attacks(neighbor)))
    
    return neighbors

def hill_climbing(n, max_iterations=1000):
    current = create_board(n)
    current_attacks = calculate_attacks(current)
    
    iterations = 0
    
    while current_attacks > 0 and iterations < max_iterations:
        neighbors = get_neighbors(current)
        best_neighbor, best_attacks = min(neighbors, key=lambda x: x[1])
        
        if best_attacks >= current_attacks:
            print(f"Stuck in local minimum at iteration {iterations}")
            break
        
        current = best_neighbor
        current_attacks = best_attacks
        iterations += 1
    
    return current, current_attacks, iterations

def print_board(board):
    n = len(board)
    print("\nBoard Configuration:")
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Run the code
n = 8
print(f"Solving {n}-Queens Problem using Hill Climbing\n")

max_attempts = 10
for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt}:")
    solution, attacks, iterations = hill_climbing(n)
    
    if attacks == 0:
        print(f"✓ Solution found in {iterations} iterations!")
        print(f"Board: {solution}")
        print_board(solution)
        break
    else:
        print(f"✗ Failed - {attacks} attacking pairs remaining")
        print()
else:
    print(f"Could not find solution in {max_attempts} attempts")
