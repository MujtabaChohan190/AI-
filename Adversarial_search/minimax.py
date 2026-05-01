import math   # Used for +infinity and -infinity

# Node class represents each state in the game tree
class Node:
    def __init__(self, value=None):
        self.value = value              # Stores node label (A, B, etc.) OR leaf value (2,3,...)
        self.children = []              # List of child nodes
        self.minmax_value = None        # Stores computed minimax value


# Agent that applies Minimax
class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth              # Maximum depth to search

    # Checks whether minimax is already computed
    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    # Agent decides what to do
    def act(self, node, environment):
        goal_status = self.formulate_goal(node)

        if goal_status == "Goal reached":
            # If already computed, return stored result
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            # Otherwise, compute minimax from root
            return environment.compute_minimax(node, self.depth)


# Environment contains the tree and minimax logic
class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []   # Keeps track of visited nodes (for understanding traversal)

    # Returns current state (not very useful here, just for structure)
    def get_percept(self, node):
        return node

    # MAIN MINIMAX FUNCTION
    def compute_minimax(self, node, depth, maximizing_player=True):

        # BASE CASE:
        # If depth is 0 OR node is a leaf → return its value
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)   # Track visited node
            return node.value

        # CASE 1: MAXIMIZING PLAYER
        if maximizing_player:
            value = -math.inf   # Start with smallest possible value

            for child in node.children:
                # RECURSIVE CALL:
                # Go to child node, reduce depth, switch to minimizing player
                child_value = self.compute_minimax(child, depth - 1, False)

                # Choose maximum among children
                value = max(value, child_value)

            node.minmax_value = value   # Store result at node
            self.computed_nodes.append(node.value)
            return value

        # CASE 2: MINIMIZING PLAYER
        else:
            value = math.inf   # Start with largest possible value

            for child in node.children:
                # RECURSIVE CALL:
                # Go to child node, reduce depth, switch to maximizing player
                child_value = self.compute_minimax(child, depth - 1, True)

                # Choose minimum among children
                value = min(value, child_value)

            node.minmax_value = value   # Store result at node
            self.computed_nodes.append(node.value)
            return value


# Function to start agent
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)   # Get current state
    agent.act(percept, environment)                 # Run minimax


# ---------------- TREE CONSTRUCTION ----------------

# Root node (Max player)
root = Node('A')

# Level 1 (Min player)
n1 = Node('B'); n2 = Node('C')
root.children = [n1, n2]

# Level 2 (Max player)
n3 = Node('D'); n4 = Node('E'); n5 = Node('F'); n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

# Level 3 (Leaf nodes with actual values)
n7 = Node(2); n8 = Node(3)
n9 = Node(5); n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0); n12 = Node(1)
n13 = Node(7); n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]


# ---------------- RUN MINIMAX ----------------

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)

run_agent(agent, environment, root)


# ---------------- OUTPUT ----------------

print("Computed Nodes:", environment.computed_nodes)

print("Minimax values:")
print("A:", root.minmax_value)   # Final answer (root)
print("B:", n1.minmax_value)
print("C:", n2.minmax_value)
