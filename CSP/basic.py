# Import the Google OR-Tools library to solve CSP problems
from ortools.sat.python import cp_model

# Declare the model and bind it with CpModel (provided by ortools)
model = cp_model.CpModel()

# Declare the set of variables for CSP
# Each variable can take values from 0 to num_vals-1 (i.e., 0, 1, or 2)
num_vals = 3
x = model.new_int_var(0, num_vals - 1, "x")  # Variable x: domain {0, 1, 2}
y = model.new_int_var(0, num_vals - 1, "y")  # Variable y: domain {0, 1, 2}
z = model.new_int_var(0, num_vals - 1, "z")  # Variable z: domain {0, 1, 2}

# Declare Constraints: x and y must have different values (Binary Constraint)
model.add(x != y)

# Create the solver and solve the model
solver = cp_model.CpSolver()
status = solver.solve(model)

# If an optimal or feasible solution is found, print the values
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.value(x)}")
    print(f"y = {solver.value(y)}")
    print(f"z = {solver.value(z)}")
else:
    print("No solution found.")

# Output:-
# x = 0
# y = 1
# z = 0



"""Simple solve."""
from ortools.sat.python import cp_model

def simple_sat_program():
    """Minimal CP-SAT example to showcase calling the solver."""
    
    # Creates the model
    model = cp_model.CpModel()

    # Creates the variables with domain {0, 1, 2}
    num_vals = 3
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Creates the constraint: x must not equal y
    model.add(x != y)

    # Creates a solver and solves the model
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Print result if a solution is found
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
    else:
        print("No solution found.")

# Call the function
simple_sat_program()

# Output:-
# x = 1
# y = 0
# z = 0
