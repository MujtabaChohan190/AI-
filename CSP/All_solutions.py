from ortools.sat.python import cp_model

# Custom callback class that prints each solution found by the solver
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables       # Store the list of variables to print
        self.__solution_count = 0          # Counter to track total solutions found

    def on_solution_callback(self) -> None:
        # Called automatically each time the solver finds a new solution
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")  # Print each variable's value
        print()  # Newline after each solution

    @property
    def solution_count(self) -> int:
        return self.__solution_count  # Getter for total solution count


def search_for_all_solutions_sample_sat():
    """Showcases calling the solver to search for all solutions."""
    
    # Creates the model
    model = cp_model.CpModel()

    # Creates the variables with domain {0, 1, 2}
    num_vals = 3
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Create the constraint: x must not equal y
    model.add(x != y)

    # Create a solver and attach the solution printer callback
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter([x, y, z])

    # Tell the solver to enumerate ALL solutions (not just the first one)
    solver.parameters.enumerate_all_solutions = True

    # Solve and pass the callback so it fires on every solution found
    status = solver.solve(model, solution_printer)

    # Print final solver status and total count of solutions
    print(f"Status = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


search_for_all_solutions_sample_sat()

# Output:-
# x=1 y=0 z=0
# x=2 y=0 z=0
# ... (18 solutions total)
# Status = OPTIMAL
# Number of solutions found: 18
