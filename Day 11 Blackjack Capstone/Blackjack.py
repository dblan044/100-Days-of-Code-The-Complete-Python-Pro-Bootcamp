"""
Rules:
Add cards up to 21
Dealers 2nd card is hidden
if you go over you lose - Bust
Cards 2-10 count as their face value
J, Q and K count as 10ea
A can count as 1 or 11
    depending on current card count, can decide what value to set
When dealer and user score is the same - Draw
If dealer hand is < 17, they must take another card
"""

import random, art

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deal = random.choice(cards)
    return deal

def calculate_score(cards):
    """Takes a list of cards that calculates a Blackjack or a score over 21"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(p_score, c_score):
    if p_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Opponent scored a Blackjack. You lose!"
    elif p_score == 0:
        return "You scored a Blackjack. You win!"
    elif p_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
         return "Opponent went over. You win!"
    elif p_score > c_score:
        return "You win!"
    else:
        return "You Lose!"

def play_game():
    print(art.logo)
    player_cards = []
    computer_cards = []
    computer_score = -1
    player_score = -1

    #add two cards to the computer and player hand
    for _ in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        #check the sum of cards for each player
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards}, current score {computer_score}")

        #check for a Blackjack for either player or a score over 21
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_another_card == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {player_cards}, final score {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 25)
    play_game()
