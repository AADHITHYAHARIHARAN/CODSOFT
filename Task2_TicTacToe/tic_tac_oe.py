import math


game_board = [" "] * 9


def show_board():
    """Display the current game board."""
    print()
    for row in range(3):
        start = row * 3
        print(
            f" {game_board[start]} | {game_board[start + 1]} | {game_board[start + 2]}"
        )
        if row < 2:
            print("---+---+---")
    print()


def has_won(symbol):
    """Return True if the given symbol has won."""
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_lines:
        if (
            game_board[a] == symbol
            and game_board[b] == symbol
            and game_board[c] == symbol
        ):
            return True

    return False


def board_full():
    """Check whether all cells are occupied."""
    return " " not in game_board


def minimax(ai_turn):
    """Evaluate the board using the Minimax algorithm."""

    if has_won("O"):
        return 1

    if has_won("X"):
        return -1

    if board_full():
        return 0

    if ai_turn:
        best_value = -math.inf

        for index in range(9):
            if game_board[index] == " ":
                game_board[index] = "O"
                value = minimax(False)
                game_board[index] = " "
                best_value = max(best_value, value)

        return best_value

    best_value = math.inf

    for index in range(9):
        if game_board[index] == " ":
            game_board[index] = "X"
            value = minimax(True)
            game_board[index] = " "
            best_value = min(best_value, value)

    return best_value


def computer_play():
    """Choose the best move for the AI."""

    highest_score = -math.inf
    best_position = None

    for index in range(9):
        if game_board[index] == " ":
            game_board[index] = "O"

            current_score = minimax(False)

            game_board[index] = " "

            if current_score > highest_score:
                highest_score = current_score
                best_position = index

    if best_position is not None:
        game_board[best_position] = "O"


def player_play():
    """Read and validate the user's move."""

    while True:
        try:
            choice = int(input("Choose a position (1-9): ")) - 1

            if choice < 0 or choice > 8:
                print("Please enter a number between 1 and 9.")
            elif game_board[choice] != " ":
                print("That position is already taken.")
            else:
                game_board[choice] = "X"
                break

        except ValueError:
            print("Invalid input. Enter a number only.")


def main():
    print("=== Tic-Tac-Toe ===")
    print("You are X")
    print("Computer is O")

    while True:
        show_board()

        player_play()

        if has_won("X"):
            show_board()
            print("You won the game!")
            break

        if board_full():
            show_board()
            print("The game ended in a draw.")
            break

        print("Computer is making its move...")
        computer_play()

        if has_won("O"):
            show_board()
            print("Computer wins!")
            break

        if board_full():
            show_board()
            print("The game ended in a draw.")
            break


if __name__ == "__main__":
    main()