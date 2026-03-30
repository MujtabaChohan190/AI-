import random

# ── PART 1: Environment ───────────────────────────
class Environment:
    def __init__(self, i, j):
        self.i = i      # current row
        self.j = j      # current column
        self.grid = [
            ["S", " ", " ", " ", " "],   # row 0 — S = start
            [" ", " ", " ", " ", " "],   # row 1
            [" ", " ", " ", " ", " "],   # row 2
            [" ", " ", " ", " ", " "],   # row 3
            [" ", " ", " ", " ", "F"],   # row 4 — F = finish
        ]

    def get_percept(self):
        # returns what's at current position + coordinates
        return (self.grid[self.i][self.j], self.i, self.j)

    def move(self, action):
        if action == "right":
            self.j += 1      # move column right
        elif action == "down":
            self.i += 1      # move row down


# ── PART 2: Utility Agent ─────────────────────────
class UtilityAgent:
    def __init__(self):
        # positive = good move, negative = bad move
        self.utility = {
            "left" : -10,   # bad — going away from goal
            "right":  10,   # good — going toward goal
            "up"   : -10,   # bad — going away from goal
            "down" :  10,   # good — going toward goal
        }

    def select_action(self, percept):
        cell, i, j = percept    # unpack percept

        if cell == "S":
            # at start — randomly go right or down
            return random.choice(["right", "down"])

        elif cell == "F":
            # at finish — done!
            return "Goal Reached"

        else:
            # somewhere in middle — pick best valid action
            while True:
                action = random.choice(list(self.utility.keys()))

                # only pick actions with positive utility
                if self.utility[action] == 10:
                    # check boundaries before moving
                    if action == "right" and j < 4:
                        return action
                    if action == "down"  and i < 4:
                        return action

    def act(self, percept):
        action = self.select_action(percept)
        return action


# ── PART 3: Run Simulation ────────────────────────
def run_agent(agent, environment):
    total_utility = 0

    while True:
        # sense
        percept = environment.get_percept()

        # decide
        action = agent.act(percept)

        # check if goal reached
        if action == "Goal Reached":
            print("🎯 Goal Reached!")
            break

        print(f"Position ({environment.i},{environment.j}) "
              f"→ Moving: {action}")

        # mark visited cell with 'r'
        environment.grid[environment.i][environment.j] = "r"

        # add utility of this action
        total_utility += agent.utility[action]

        # actually move
        environment.move(action)

    # print total utility
    print(f"\nTotal Utility: {total_utility}")

    # print final grid
    print("\nFinal Grid:")
    for i in range(5):
        for j in range(5):
            print(f"{environment.grid[i][j]} ", end="")
        print()


# ── Run ───────────────────────────────────────────
e1 = Environment(0, 0)
u1 = UtilityAgent()
run_agent(u1, e1)
```

---

Now let me explain everything! 🎯

---

# 🧠 Big Picture First
```
5x5 grid:
S = Start (0,0)  top-left
F = Finish (4,4) bottom-right

Agent must go from S to F
Only allowed moves: RIGHT or DOWN
Each good move = +10 utility
