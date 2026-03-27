import random

# =========================
# Heuristic Function
# =========================
# Counts the number of pairs of attacking queens
def calculate_conflicts(state):
    """
    Input: state = list of queen positions; index = row, value = column
    Output: total number of attacking pairs (conflicts)
    """
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            # Check if same column or diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# =========================
# Generate Neighbors
# =========================
# Create all possible neighbor states by moving one queen at a time
def get_neighbors(state):
    neighbors = []
    n = len(state)

    for row in range(n):
        for col in range(n):
            if col != state[row]:  # Skip column where queen is already present
                new_state = list(state)
                new_state[row] = col
                neighbors.append(new_state)

    return neighbors


# =========================
# Simple Hill Climbing
# =========================
def simple_hill_climbing(n):
    """
    Hill Climbing for N-Queens
    Returns a state (list of queen positions) and its conflicts
    """
    # Start with a random state
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = calculate_conflicts(current_state)

    while True:
        neighbors = get_neighbors(current_state)

        next_state = None
        next_conflicts = current_conflicts

        # Find the first neighbor that improves the state
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)

            if neighbor_conflicts < next_conflicts:
                next_state = neighbor
                next_conflicts = neighbor_conflicts
                break  # Stop at first improvement

        # If no improvement found, we are stuck at local minimum
        if next_conflicts >= current_conflicts:
            break

        # Move to the better neighbor
        current_state = next_state
        current_conflicts = next_conflicts

    return current_state, current_conflicts


# =========================
# Run Hill Climbing
# =========================
n = 8
solution, conflicts = simple_hill_climbing(n)

if conflicts == 0:
    print("Solution found:", solution)
else:
    print("Stuck with conflicts:", conflicts)
    print("State:", solution)


# =========================
# Explanation
# =========================
"""
Part 1: Why do we count conflicts?

In Hill Climbing for N-Queens, the goal is to find a board configuration
where no two queens attack each other (0 conflicts).

- Conflicts are our "badness measure":
    - Each pair of queens attacking each other adds 1 conflict.
    - More conflicts → worse state
    - 0 conflicts → perfect solution

- The hill climbing algorithm uses this measure to decide
  whether a neighbor is better than the current state.

- It moves to neighbors with fewer conflicts until:
    a) a solution (0 conflicts) is found, or
    b) it reaches a local minimum (stuck with no better neighbors)
"""
