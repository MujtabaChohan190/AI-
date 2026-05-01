#Find the best assignment (maximum value) under constraints”

# Install ortools if not already installed
# %pip install ortools

from ortools.sat.python import cp_model

def main() -> None:
    """Minimal CP-SAT example to showcase calling the solver with optimization."""
    
    # Creates the model
    model = cp_model.CpModel()

    # Set the upper bound for all variables as the max of the constraint bounds
    var_upper_bound = max(50, 45, 37)  # = 50

    # Create integer variables x, y, z each with domain [0, 50]
    x = model.new_int_var(0, var_upper_bound, "x")
    y = model.new_int_var(0, var_upper_bound, "y")
    z = model.new_int_var(0, var_upper_bound, "z")

    # Define the inequality constraints (feasible region boundaries)
    model.add(2 * x + 7 * y + 3 * z <= 50)   # Constraint 1
    model.add(3 * x - 5 * y + 7 * z <= 45)   # Constraint 2
    model.add(5 * x + 2 * y - 6 * z <= 37)   # Constraint 3

    # Define the objective function to maximize
    model.maximize(2 * x + 2 * y + 3 * z)

    # Create the solver and solve
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Print the optimal values if a solution is found
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Maximum of objective function: {solver.objective_value}\n")
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
    else:
        print("No solution found.")

    # Print solver statistics for analysis
    print("\nStatistics")
    print(f"  status   : {solver.status_name(status)}")
    print(f"  conflicts: {solver.num_conflicts}")
    print(f"  branches : {solver.num_branches}")
    print(f"  wall time: {solver.wall_time} s")


main()

# Output:-
# Maximum of objective function: 35.0
# x = 7
# y = 3
# z = 5
# Statistics
#   status   : OPTIMAL
#   conflicts: 3
#   branches : 14
#   wall time: 0.016781573 s
