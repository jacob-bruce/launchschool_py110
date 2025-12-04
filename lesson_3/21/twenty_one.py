"""

ALGORITHM:
1. Initialize deck X
2. Deal cards to player and dealer X
3. Player turn: hit or stay
   - repeat until bust or stay

    - Print something about it being the player's turn
    - Ask player if they'd like to hit or stay
        - if the total of their cards is under 21, ask again
        - if it exceeds 21, game over

4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17

- Check hand. If total is less than 17, hit.
- If 



6. If dealer busts, player wins.
7. Compare cards and declare winner.

Add messages for thinking
dealer code and hits
_____________________



"""
import random
import os
import time

TWENTY_ONE = 21
STAY = ['stay', 's']
HIT = ['hit', 'h']
YES = ['yes', 'y', 'yeah']
NO = ['no', 'nope', 'n']
INITIAL_HAND_SIZE = 2
WIDTH = 60
TABLE_WIDTH  = 50
WELCOME_MESSAGE = """
Welcome to Twenty-One

The goal of the game is to have the hand value closest to 21. 
You and the dealer will be dealt two cards, though you can each
only see one of each other's cards. After receiving your initial
two cards, you can decide whether to receive additional cards by
'hitting.' Be careful though—-if your hand value goes over 21 you 
will 'bust' and the dealer will win by default. Once you are 
comfortable with your hand, you 'stay' and its the dealer's turn. 
If neither you nor the dealer 'bust,' the person with the hand 
value closest to 21 wins. Card values are as follows:

2-10: Face Value
J-K: 10
A: Can be 1 or 11

Good luck!
"""

def prompt(message):
    """Stylizes print message"""
    print(f'==> {message}')

def welcome_message():

    print(f"{'*' * TABLE_WIDTH}".center(WIDTH, ' '))
    print(f"{WELCOME_MESSAGE}".center(WIDTH, ' '))
    print()

    while True:
        prompt("Press 'y' to continue")
        answer = input().lower().strip()
        if answer in YES:
            break
        else:
            print("Invalid choice. Please try again.")


def initialize_deck():
    """Creates a deck of cards"""
    suits = ['♥', '♣', '♦', '♠']
    values = ['A', '2', '3', '4', '5', '6',
              '7', '8', '9', '10',
              'J', 'Q', 'K'
              ]
    return [[suit, value] for suit in suits
                          for value in values]

def display_table(player_hand, dealer_hand, dealer_hand_display, message = ''):
    """Displays the table based on whether player should see dealer's cards"""
    
    if dealer_hand_display:
        dealer_hand_display = make_dealer_hand_display(dealer_hand)
    else:
        dealer_hand_display = dealer_hand

    total = calculate_hand(player_hand)
    os.system('clear')
    print()
    print(f"{'=' * TABLE_WIDTH}".center(WIDTH, ' '))
    print()
    print("DEALER".center(WIDTH, ' '))
    print(str(dealer_hand_display).center(WIDTH, ' '))
    print()
    print()
    print()
    print(str(player_hand).center(WIDTH, ' '))
    print("PLAYER".center(WIDTH, ' '))
    print(f"Your total is {total}".center(WIDTH, ' '))
    print()
    print(f"{'=' * TABLE_WIDTH}".center(WIDTH, ' '))
    print()
    print(message)

def make_dealer_hand_display(dealer_hand):
    """Makes the dealer's hand invisible"""
    if dealer_hand:
        unknown_cards = ['???']
        num_unknown_cards = len(dealer_hand) - 1
        dealer_hand_display = [dealer_hand[0]]
        dealer_hand_display.extend([unknown_cards] * num_unknown_cards)
        return dealer_hand_display
    return []

def shuffle_deck(deck):
    """Shuffles the deck"""
    random.shuffle(deck)

def deal_hand(deck, player_hand, dealer_hand, hide_dealer_cards):
    """Deals the initial hands"""
    current_hand_size = 0

    display_table(player_hand, dealer_hand, hide_dealer_cards)
    time.sleep(.5)

    while current_hand_size != INITIAL_HAND_SIZE:
        player_hand.append(deck.pop(0))
        display_table(player_hand, dealer_hand, hide_dealer_cards)
        time.sleep(.5)
        dealer_hand.append(deck.pop(0))
        display_table(player_hand, dealer_hand, hide_dealer_cards)
        time.sleep(.5)
        current_hand_size +=1

def deal_one(deck, hand):
    """Deals one if player/dealer hits"""
    hand.append(deck.pop(0))

def player_turn(deck, player_hand, dealer_hand, hide_dealer_cards):
    """Operations for the player's turn"""
    while True:
        prompt("Hit or stay?")
        answer = input()

        if answer.lower().strip() in STAY:
            return True

        elif answer.lower().strip() in HIT:
            deal_one(deck, player_hand)
            display_table(player_hand, dealer_hand, hide_dealer_cards)

        else:
            prompt("Please enter 'hit'/'h' or 'stay'/'s'")

        if busted(player_hand):
            return False

def dealer_turn(deck, dealer_hand, player_hand, hide_dealer_cards):
    """Operations for the dealer's turn"""
    hits = 0
    dealer_actions_msg = "Dealer is thinking..."

    while True:
        if calculate_hand(dealer_hand) < 17:
            deal_one(deck, dealer_hand)
            display_table(player_hand, dealer_hand, hide_dealer_cards)
            print("Dealer hits!")
            time.sleep(1)
        elif busted(dealer_hand):
            return False
        elif calculate_hand(dealer_hand) >= 17:
            display_table(player_hand, dealer_hand, hide_dealer_cards)
            print("Dealer stays!")
            time.sleep(1)
            return True

def busted(hand):
    """Returns true if hand value > 21"""
    return calculate_hand(hand) > 21

def calculate_hand(hand):
    """Calculates the value of a hand"""
    values = [card[1] for card in hand]

    sum_val = 0
    for value in values:
        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    aces = values.count("A")

    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

def player_busted(dealer_hand, player_hand, hide_dealer_cards):
    """End game operations if player busts"""
    hide_dealer_cards = False
    display_table(player_hand, dealer_hand, hide_dealer_cards)
    print(f"Shoot! You busted with a hand value of {calculate_hand(player_hand)}! "
          f"The dealer had {calculate_hand(dealer_hand)}.")

def dealer_busted(dealer_hand, player_hand, hide_dealer_cards):
    """End game operations if dealer busts"""
    hide_dealer_cards = False
    display_table(player_hand, dealer_hand, hide_dealer_cards)
    print(f"The dealer busted with a hand value of {calculate_hand(dealer_hand)}! You won!")

def determine_winner(dealer_hand, player_hand, hide_dealer_cards):
    """Determines winner if no one busts"""
    dealer = calculate_hand(dealer_hand)
    player = calculate_hand(player_hand)
    hide_dealer_cards = False

    display_table(player_hand, dealer_hand, hide_dealer_cards)

    if dealer > player:
        print(f'Dang! Dealer wins {dealer} to {player}. Looks like the dealer got you this time.')
    elif player > dealer:
        print(f'You beat the dealer {player} to {dealer}! Well done!')
    elif player == dealer:
        print(f"Wow a tie, {dealer} to {player}. Don't see that very often!")

def play_twenty_one():
    """Initializes game"""
    os.system('clear')
    welcome_message()

    while True:
        hide_dealer_cards = True
        dealer_hand = []
        player_hand = []
        dealer_result = None
        player_result = None

        deck = initialize_deck()
        shuffle_deck(deck)
        deal_hand(deck, player_hand, dealer_hand, hide_dealer_cards)

        player_result = player_turn(deck, player_hand, dealer_hand, hide_dealer_cards)

        if player_result:
            dealer_result = dealer_turn(deck, dealer_hand, player_hand, hide_dealer_cards)
        
            if dealer_result:
                determine_winner(dealer_hand, player_hand, hide_dealer_cards)
            else:
                dealer_busted(dealer_hand, player_hand, hide_dealer_cards)
        else:
            player_busted(dealer_hand, player_hand, hide_dealer_cards)

        while True:
            prompt("Play again? (y or n)")
            answer = input().lower()
            if answer in YES:
                break
            elif answer in NO:
                prompt('Thanks for playing!')
                return
            else:
                print("Invalid choice. Please try again.")

play_twenty_one()
