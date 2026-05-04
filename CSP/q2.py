# ─────────────────────────────────────────────────────────────
#  University Wardrobe Scheduler using OR-Tools CP-SAT
#  Resources : SQ×2, Shirts×5, Pants×3  →  17 unique outfits
#  Outfits   : 0-1 = SQ sets, 2-16 = Shirt+Pant combinations
#  Constraints:
#    - Monday & Thursday → must wear Shirt-Pant (outfit ≥ 2)
#    - Friday            → must wear Shalwar Qamees (outfit ≤ 1)
#    - All 5 days        → each outfit is unique (all_different)
# ─────────────────────────────────────────────────────────────
from ortools.sat.python import cp_model

# Custom callback class that prints each valid weekly schedule
class WardrobeSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print all valid 5-day wardrobe schedules."""

    def __init__(self, variables: list[cp_model.IntVar], day_names: list[str]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables     = variables
        self.__day_names     = day_names
        self.__solution_count = 0

    def outfit_name(self, idx: int) -> str:
        # Convert outfit index to a readable label
        if idx == 0: return "SQ-Set1"
        if idx == 1: return "SQ-Set2"
        shirt = (idx - 2) // 3 + 1   # shirt number  (1-5)
        pant  = (idx - 2) %  3 + 1   # pant number   (1-3)
        return f"Shirt{shirt}+Pant{pant}"

    def on_solution_callback(self) -> None:
        # Called automatically each time solver finds a valid schedule
        self.__solution_count += 1
        print(f"Solution {self.__solution_count}: ", end="")
        for v, d in zip(self.__variables, self.__day_names):
            print(f"{d}={self.outfit_name(self.value(v))}", end="  ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count


def wardrobe_scheduler_csp():
    """Find all valid wardrobe schedules for a 5-day university week."""

    # Create the CP-SAT model
    model = cp_model.CpModel()

    # Days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # 17 unique outfits: indices 0-1 are SQ sets, indices 2-16 are Shirt+Pant
    num_outfits = 17   # 2 SQ  +  (5 shirts × 3 pants = 15)

    # One variable per day — domain is the full outfit catalogue
outfit = []

for i in range(5):
    var = model.new_int_var(0, num_outfits - 1, days[i])
    outfit.append(var)

    # Constraint 1: every day must have a UNIQUE outfit
    model.add_all_different(outfit)

    # Constraint 2: Monday (idx 0) → must wear Shirt-Pant (outfit ≥ 2)
    model.add(outfit[0] >= 2)

    # Constraint 3: Thursday (idx 3) → must wear Shirt-Pant (outfit ≥ 2)
    model.add(outfit[3] >= 2)

    # Constraint 4: Friday (idx 4) → must wear Shalwar Qamees (outfit ≤ 1)
    model.add(outfit[4] <= 1)

    # Create solver and attach the solution-printing callback
    solver = cp_model.CpSolver()
    solution_printer = WardrobeSolutionPrinter(outfit, days)

    # Tell solver to enumerate ALL solutions, not just the first one
    solver.parameters.enumerate_all_solutions = True

    # Solve and fire callback on every valid schedule found
    status = solver.solve(model, solution_printer)

    print(f"\nStatus = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


wardrobe_scheduler_csp()
