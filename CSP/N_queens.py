import sys
import time
from ortools.sat.python import cp_model

# Declare the model
model = cp_model.CpModel()

# Board size: 8x8 chessboard (can be changed to any N)
board_size = 8

# One variable per column; the variable's value = the row the queen is placed in
# Domain of each variable: 0 to board_size-1 (valid row indices)
queens = [model.new_int_var(0, board_size - 1, f"x_{i}") for i in range(board_size)]

# Constraint 1: All queens must be in different rows (no two queens share a row)
model.add_all_different(queens)

# Constraint 2: No two queens share the same "down-right" diagonal
# queens[i] + i gives a unique diagonal identifier for each queen
model.add_all_different(queens[i] + i for i in range(board_size))

# Constraint 3: No two queens share the same "down-left" diagonal
# queens[i] - i gives a unique anti-diagonal identifier for each queen
model.add_all_different(queens[i] - i for i in range(board_size))

# Additional diagonal constraint using explicit auxiliary variables
diag1 = []
for i in range(board_size):
    # Create an auxiliary variable to represent the diagonal offset
    q1 = model.NewIntVar(0, 2 * board_size, 'diag1_%i' % i)
    diag1.append(q1)
    # Link auxiliary variable to the queen's position + column index
    model.Add(q1 == queens[i] + i)

# Ensure all diagonal offsets are different (no shared diagonal)
model.AddAllDifferent(diag1)


# ── Solution Printer Callback ─────────────────────────────────────────────────
class NQueenSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables       # Store the list of variables
        self.__solution_count = 0          # Counter to track total solutions found
        self.__start_time = time.time()    # Record start time for timing each solution

    @property
    def solution_count(self) -> int:
        return self.__solution_count       # Getter for total solution count

    def on_solution_callback(self) -> None:
        # Called automatically each time the solver finds a new solution
        self.__solution_count += 1

        # Print each variable and its assigned value on one line
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()   # Newline after each solution


# ── Solve ─────────────────────────────────────────────────────────────────────

# Create solver and attach the solution printer
solver = cp_model.CpSolver()
solution_printer = NQueenSolutionPrinter(queens)

# Enumerate all solutions (not just the first)
solver.parameters.enumerate_all_solutions = True

# Solve the model and trigger the callback for each solution found
status = solver.solve(model, solution_printer)

# Print final status and total number of solutions found
print(f"Status = {solver.status_name(status)}")
print(f"Number of solutions found: {solution_printer.solution_count}")

# Output (first solution shown):
# Q _ _ _ _ _ _ _
# _ _ _ _ _ _ Q _
# _ _ _ _ Q _ _ _
# _ _ _ _ _ _ _ Q
# _ Q _ _ _ _ _ _
# _ _ _ Q _ _ _ _
# _ _ _ _ _ Q _ _
# _ _ Q _ _ _ _ _
# ...91 other solutions displayed...
# Solutions found: 92
