import math

# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, board, player):
        self.board = board              # Current board state (3x3)
        self.player = player            # Current player ('X' or 'O')
        self.children = []              # Possible next states
        self.minmax_value = None        # Store minimax value


# ---------------- AGENT ----------------
class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return node.minmax_value
        else:
            return environment.compute_minimax(node, self.depth, True)


# ---------------- ENVIRONMENT ----------------
class Environment:
    def __init__(self):
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    # Check winner
    def check_winner(self, board):
        win_states = [
            [0,1,2],[3,4,5],[6,7,8],   # rows
            [0,3,6],[1,4,7],[2,5,8],   # cols
            [0,4,8],[2,4,6]            # diagonals
        ]
        for state in win_states:
            if board[state[0]] == board[state[1]] == board[state[2]] != ' ':
                return board[state[0]]
        return None

    # Check draw
    def is_draw(self, board):
        return ' ' not in board

    # Generate children
    def generate_children(self, node):
        next_player = 'O' if node.player == 'X' else 'X'
        for i in range(9):
            if node.board[i] == ' ':
                new_board = node.board.copy()
                new_board[i] = node.player
                child = Node(new_board, next_player)
                node.children.append(child)

    # MINIMAX FUNCTION
    def compute_minimax(self, node, depth, maximizing_player):

        winner = self.check_winner(node.board)

        # BASE CASE
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        elif self.is_draw(node.board) or depth == 0:
            return 0

        self.generate_children(node)

        # MAX PLAYER (Computer = X)
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.compute_minimax(child, depth-1, False))
            node.minmax_value = value
            return value

        # MIN PLAYER (User = O)
        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.compute_minimax(child, depth-1, True))
            node.minmax_value = value
            return value


# ---------------- GAME FUNCTIONS ----------------
def print_board(board):
    print("\n")
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print("\n")


def best_move(environment, board):
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            new_board = board.copy()
            new_board[i] = 'X'
            node = Node(new_board, 'O')

            move_val = environment.compute_minimax(node, 5, False)

            if move_val > best_val:
                best_val = move_val
                move = i

    return move


# ---------------- MAIN GAME ----------------
def play_game():
    board = [' '] * 9
    env = Environment()

    while True:
        print_board(board)

        # USER MOVE
        user_move = int(input("Enter position (0-8): "))
        if board[user_move] != ' ':
            print("Invalid move!")
            continue

        board[user_move] = 'O'

        if env.check_winner(board) == 'O':
            print_board(board)
            print("You win!")
            break

        if env.is_draw(board):
            print_board(board)
            print("Draw!")
            break

        # COMPUTER MOVE
        comp_move = best_move(env, board)
        board[comp_move] = 'X'
        print(f"Computer plays at {comp_move}")

        if env.check_winner(board) == 'X':
            print_board(board)
            print("Computer wins!")
            break

        if env.is_draw(board):
            print_board(board)
            print("Draw!")
            break


# ---------------- RUN ----------------
play_game()
