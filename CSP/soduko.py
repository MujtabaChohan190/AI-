from ortools.sat.python import cp_model

def solve_sudoku():

    # Puzzle definition — 0 means empty cell
    given = [
        [0, 0, 6, 2, 0, 5],
        [0, 0, 0, 4, 6, 0],
        [0, 1, 2, 0, 0, 0],
        [5, 6, 0, 0, 0, 4],
        [0, 0, 4, 3, 0, 2],
        [3, 0, 0, 5, 0, 6],
    ]

    # Create the model
    model = cp_model.CpModel()

    # Declare variables — 6x6 grid, each cell has domain {1, 2, 3, 4, 5, 6}
    grid = [
        [model.new_int_var(1, 6, f"cell_{r}_{c}") for c in range(6)]
        for r in range(6)
    ]

    # Fix pre-filled cells — force variable to the given value
    for r in range(6):
        for c in range(6):
            if given[r][c] != 0:
                model.add(grid[r][c] == given[r][c])

    # Row constraint — all digits in each row must be different
    for r in range(6):
        model.add_all_different(grid[r])

    # Column constraint — all digits in each column must be different
    for c in range(6):
        model.add_all_different([grid[r][c] for r in range(6)])

    # Sub-grid constraint — each 2x3 box must contain digits 1–6 exactly once
    for box_row in range(3):
        for box_col in range(2):
            cells = []
            for r in range(box_row * 2, box_row * 2 + 2):
                for c in range(box_col * 3, box_col * 3 + 3):
                    cells.append(grid[r][c])
            model.add_all_different(cells)

    # Create solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Print the solved grid if a solution is found
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solved Sudoku:\n")
        for r in range(6):
            print(" ".join(str(solver.value(grid[r][c])) for c in range(6)))
    else:
        print("No solution found.")


solve_sudoku()
