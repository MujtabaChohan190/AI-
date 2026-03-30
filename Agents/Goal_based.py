# ── PART 1: Environment ───────────────────────────
class Environment:
    def __init__(self, state="Dirty"):
        # ↑ MODIFY THIS: change initial state
        self.state = state

    def get_percept(self):
        return self.state          # returns current state to agent

    def clean_room(self):
        self.state = "Clean"       # updates environment


# ── PART 2: Goal Based Agent ──────────────────────
class GoalBasedAgent:
    def __init__(self):
        self.goal = None           # agent starts with no goal

    def formulate_goal(self, percept):
        # ↑ MODIFY THIS: change goal logic based on problem
        if percept == "Dirty":
            self.goal = "Clean"         # set goal
        else:
            self.goal = "No action"     # no goal needed

    def act(self, percept):
        self.formulate_goal(percept)    # step 1: set goal

        # step 2: act to achieve goal
        # ↑ MODIFY THIS: change actions based on problem
        if self.goal == "Clean":
            return "Clean the room"
        else:
            return "Room is already clean"


# ── PART 3: Simulation ────────────────────────────
def run_agent(agent, environment, steps):
    # ↑ MODIFY THIS: change steps number
    for step in range(steps):

        # sense
        percept = environment.get_percept()

        # decide
        action = agent.act(percept)

        # print
        print(f"Step {step+1}: Percept - {percept}, "
              f"Goal - {agent.goal}, Action - {action}")

        # update environment
        # ↑ MODIFY THIS: change how environment updates
        if percept == "Dirty":
            environment.clean_room()


# ── Run ───────────────────────────────────────────
agent       = GoalBasedAgent()
environment = Environment()         # ← change initial state here
run_agent(agent, environment, 5)    # ← change steps here
```

---

## Output:
```
Step 1: Percept - Dirty, Goal - Clean,     Action - Clean the room
Step 2: Percept - Clean, Goal - No action, Action - Room is already clean
Step 3: Percept - Clean, Goal - No action, Action - Room is already clean
Step 4: Percept - Clean, Goal - No action, Action - Room is already clean
Step 5: Percept - Clean, Goal - No action, Action - Room is already clean
