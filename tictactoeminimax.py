# Define two constants to track the current player.
# MAX is the human Player
# MIN is the AI Player
MAX = 1
MIN = -1

# Define the board as 3x3 grid
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# the print_board() will print the board, by looping through all the rows
def print_board():
    symbols = {0: " ", 1: "X", -1: "O"}
    for row in board:
        print(symbols[row[0]] + "|" + symbols[row[1]] + "|" + symbols[row[2]])
    print()

# the empty_cells() will return all the list of empty cells in the board
def empty_cells():
    cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                cells.append([i, j])
    return cells

# wins() will check which player has won
def wins(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def evaluate():
    if wins(MAX):
        return 1
    elif wins(MIN):
        return -1
    else:
        return 0

# Here we will implement the minimax function with the alpha, beta parameters
def minimax(player, alpha, beta):
    # First of all, we have to check for the base case -> If a game is over or the board is full
    if wins(MAX) or wins(MIN) or len(empty_cells()) == 0:
        return None, evaluate()

    # If it`s our turn, then we want to maximize the score
    if player == MAX:
        best_score = -1000
        best_move = None
        for cell in empty_cells():
            i, j = cell
            board[i][j] = MAX
            _, score = minimax(MIN, alpha, beta)
            board[i][j] = 0
            if score > best_score:
                best_score = score
                best_move = [i, j]
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
    else:
        # In this case, it`s AI s turn
        best_score = 1000
        best_move = None
        for cell in empty_cells():
            i, j = cell
            board[i][j] = MIN
            _, score = minimax(MAX, alpha, beta)
            board[i][j] = 0
            if score < best_score:
                best_score = score
                best_move = [i, j]
            beta = min(beta, best_score)
            if beta <= alpha:
                break

    return best_move, best_score

# human_turn() will accept our values
def human_turn():
    print("Your turn! Enter 1-9:")
    while True:
        move = input()
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                i = (move-1)//3
                j = (move-1)%3
                if board[i][j] == 0:
                    board[i][j] = MAX
                    break
                else:
                    print("Cell occupied, try again.")
            else:
                print("Enter a number 1-9.")
        else:
            print("Invalid input, try again.")

# AI will choose its moves based on the MiniMax Algorithm
def ai_turn():
    move, _ = minimax(MIN, -1000, 1000)
    i, j = move
    board[i][j] = MIN
    print("AI moved:")

# This is the game loop
def main():
    print("Tic-Tac-Toe! You are X, AI is O")
    print_board()
    while True:
        human_turn()
        print_board()
        if wins(MAX):
            print("You win!")
            break
        if len(empty_cells()) == 0:
            print("Draw!")
            break
        ai_turn()
        print_board()
        if wins(MIN):
            print("AI wins!")
            break
        if len(empty_cells()) == 0:
            print("Draw!")
            break

if __name__ == "__main__":
    main()
