import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None


class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            # SAME as minimax, just calling alpha-beta now
            return environment.compute_alpha_beta(node, self.depth)


class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    # SAME STYLE AS compute_minimax
    def compute_alpha_beta(self, node, depth, maximizing_player=True, alpha=-math.inf, beta=math.inf):

        # BASE CASE (same as minimax)
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value

        # MAX PLAYER
        if maximizing_player:
            value = -math.inf

            for child in node.children:
                # SAME recursion idea
                child_value = self.compute_alpha_beta(child, depth - 1, False, alpha, beta)

                value = max(value, child_value)

                # NEW: update alpha
                alpha = max(alpha, value)

                # NEW: pruning condition
                if beta <= alpha:
                    break

            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

        # MIN PLAYER
        else:
            value = math.inf

            for child in node.children:
                # SAME recursion idea
                child_value = self.compute_alpha_beta(child, depth - 1, True, alpha, beta)

                value = min(value, child_value)

                # NEW: update beta
                beta = min(beta, value)

                # NEW: pruning condition
                if beta <= alpha:
                    break

            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)
