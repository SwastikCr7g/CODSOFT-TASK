import math
board = [' ' for _ in range(9)]
def print_board(board):
    for i in range(0, 9, 3):
        print('|'.join(board[i:i + 3]))
        if i < 6:
            print("-----")
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_full(board):
    return ' ' not in board
def minimax(board, depth, alpha, beta, is_maximizing):

    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_full(board):
        return 0  # Draw


    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval

    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI move
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '  # Undo move
            if score > best_score:
                best_score = score
                move = i
    return move
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human's move
        move = int(input("Enter your move (0-8): "))
        if board[move] == ' ':
            board[move] = 'X'
        else:
            print("This position is already taken.")
            continue

        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI's move:")
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
