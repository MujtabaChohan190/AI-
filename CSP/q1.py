#  Colors: 0=Red, 1=Green, 2=Blue
# ─────────────────────────────────────────────────────────────
from ortools.sat.python import cp_model

# Custom callback class that prints each solution found
class ColorSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print all valid graph colorings."""

    def __init__(self, variables: list[cp_model.IntVar], names: list[str]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables   = variables
        self.__names       = names
        self.__solution_count = 0
        self.__color_map   = {0: 'Red', 1: 'Green', 2: 'Blue'}

    def on_solution_callback(self) -> None:
        # Called automatically each time solver finds a valid coloring
        self.__solution_count += 1
        print(f"Solution {self.__solution_count}: ", end="")
        for v, n in zip(self.__variables, self.__names):
            print(f"{n}={self.__color_map[self.value(v)]}", end="  ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count


def graph_coloring_csp():
    """Find all valid 3-colorings of the given graph."""

    # Create the CP-SAT model
    model = cp_model.CpModel()

    # Declare variables — each node gets a color in {0=Red, 1=Green, 2=Blue}
    num_colors = 3
    A = model.new_int_var(0, num_colors - 1, "A")
    B = model.new_int_var(0, num_colors - 1, "B")
    C = model.new_int_var(0, num_colors - 1, "C")
    D = model.new_int_var(0, num_colors - 1, "D")
    E = model.new_int_var(0, num_colors - 1, "E")

    # Constraints: adjacent nodes must have different colors
    model.add(B != A)   # edge B-A
    model.add(B != C)   # edge B-C
    model.add(B != D)   # edge B-D
    model.add(A != D)   # edge A-D
    model.add(A != E)   # edge A-E
    model.add(D != E)   # edge D-E

    # Create solver and attach the solution-printing callback
    solver = cp_model.CpSolver()
    solution_printer = ColorSolutionPrinter([A, B, C, D, E], ["A", "B", "C", "D", "E"])

    # Tell solver to enumerate ALL solutions, not just the first one
    solver.parameters.enumerate_all_solutions = True

    # Solve and fire callback on every valid coloring found
    status = solver.solve(model, solution_printer)

    print(f"\nStatus = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


graph_coloring_csp()
