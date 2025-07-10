"""
print game name logo (outside of loop)
print option A and pertaining info minus the follower count (this must be random)
print VS logo
print option B, same stuff as A
ask the user who has more followers
    if answer is correct, print score
        have a variable that keeps track of the score and updates as the game progresses
option A will now be the previous B
    make variable A equal to the previous B
loop all of the above
    will need a while loop that ends when user gets an answer wrong
        exit loop once an answer is wrong
        print the final score
"""

import art, random
from game_data import data

def random_account():
    """Generates random celebrity information"""
    return random.choice(data)

def format_data(account):
    """Format account data into a printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def compare_follower_count(guess, a_followers, b_followers):
    """Takes user guess and follower counts to perform a vs b comparison"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

print(art.logo)
score = 0
option_b = random_account()

game_should_continue = True

while game_should_continue:
    option_a = option_b
    option_b = random_account()
    if option_a == option_b:
        option_b = random_account()

    a_follower_count = option_a['follower_count']
    b_follower_count = option_b['follower_count']

    print(f"Compare A: {format_data(option_a)}")
    print(art.vs)
    print(f"Against B: {format_data(option_b)}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    print("\n" * 20)
    print(art.logo)

    is_correct = compare_follower_count(user_guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score is {score}")
        game_should_continue = False
        
    