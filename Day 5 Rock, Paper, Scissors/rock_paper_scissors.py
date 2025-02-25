import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#calc random choice for computer (done)
#compare random choice with user choice
#based on comparison determine game result: win, lose, draw

choice_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.choice(choice_list)

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print(f"Computer choice:\n {computer_choice}")

#rock draw
if user_choice == 0 and computer_choice == choice_list[0]:
    print("Draw!")
#paper draw
elif user_choice == 1 and computer_choice == choice_list[1]:
    print("Draw!")
#scissors draw
elif user_choice == 2 and computer_choice == choice_list[2]:
    print("Draw!")
# rock wins against scissors
elif user_choice == 0 and computer_choice == choice_list[2]:
    print("You Win!")
#paper wins against rock
elif user_choice == 1 and computer_choice == choice_list[0]:
    print("You Win!")
#scissors win against paper
elif user_choice == 2 and computer_choice == choice_list[1]:
    print("You Win!")
else:
    print("You Lose!")