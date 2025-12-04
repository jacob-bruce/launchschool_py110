import random
import os

PLAYER = 'choose'
YES = ['yes', 'y', 'yeah']
NO = ['no', 'nope', 'n']
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 5
WINNING_LINES = [
  [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
  [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
  [1, 5, 9], [3, 5, 7]             # diagonals
]

def prompt(message):
    print(f"=> {message}")

def join_or(lst = [], delimiter = ',', word = 'or'):
    result = ''
    delimiter = delimiter.strip()
    
    if not lst:
        return ''
    elif len(lst) == 1:
        return f'{lst[0]}'
    elif len(lst) == 2:
        return f'{lst[0]} {word} {lst[1]}'
    else:
        for idx, item in enumerate(lst):
            if idx == len(lst) - 1:
                result += f'{word} {item}'
            else:
                result += f'{item}{delimiter} '
    
    return result

def display_board(board, computer_score, player_score):
    os.system('clear')

    print(f'SCORE: Computer - {computer_score} | Player: {player_score}')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def computer_chooses_square(board):
    square = None

    # offense
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break
    
    # defense
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break

    if not square and 5 in empty_squares(board):
        square = 5
            
    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def update_and_display_scores(board, player_score, computer_score):
    winner = detect_winner(board)
    
    if winner == 'Player':
        player_score += 1
    elif winner == 'Computer':
        computer_score += 1

    if player_score == GAMES_TO_WIN:
        print(f'PLAYER IS VICTORIOUS, {player_score} to {computer_score}! Well done!')
    elif computer_score == GAMES_TO_WIN:
        print(f'The AIs have won this won, {computer_score} to {player_score}! Better luck next time!')
    elif player_score == computer_score:
        print(f'The game is tied {player_score} to {computer_score}.')
    elif player_score > computer_score:
        print(f'Player is winning {player_score} to {computer_score}!')
    elif computer_score > player_score:
        print(f'Computer is winning {computer_score} to {player_score}!')

    return player_score, computer_score

def alternate_player(current_player):
    return 'computer' if current_player == 'player' else 'player'

def choose_square(board, current_player):
    if current_player == 'player':
        player_chooses_square(board)
    elif current_player == 'computer':
        computer_chooses_square(board)

def play_tic_tac_toe():
    player_score = 0
    computer_score = 0
    
    while True:
        board = initialize_board()

        current_player = choose_first_player()

        while True:
            display_board(board, player_score, computer_score)
            choose_square(board, current_player)
            current_player = alternate_player(current_player)
            if someone_won(board) or board_full(board):
                break

        display_board(board, player_score, computer_score)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        # Update Scores
        player_score, computer_score = update_and_display_scores(board, player_score, computer_score)
        print(f'SCORE: Computer - {computer_score} | Player: {player_score}')

        while True:
            prompt("Play again? (y or n)")
            answer = input().lower()
            if answer in YES:
                break
            elif answer in NO:
                prompt('Thanks for playing Tic Tac Toe!')
                return
            else:
                print("Invalid choice. Please try again.")


def choose_first_player():
    if PLAYER != 'choose':
        return PLAYER
    else:
        while True:
            choice = input("Who should go first (player/computer)? ").lower()
            if choice == "player":
                prompt("You're going first! Good luck!")
                return choice
            elif choice == 'computer':
                prompt("The computer will go first! You've got this! ")
                return choice
            else:
                print("Invalid choice. Please try again")

play_tic_tac_toe()