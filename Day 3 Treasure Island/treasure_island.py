print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You have entered a cave with two paths. One path leads to treasure, the other"
                " leads to your doom!\n Type 'left' or 'right.\n").lower()

if choice1 == "left":
    choice2 = input("There is a torch on the wall. Do you grab it or continue in the dark?\n "
                    "Type 'grab' to grab the torch or type 'continue' to continue through the cave\n").lower()
    if choice2 == "grab":
        choice3 = input("There is a treasure goblin at the end of the room. Charge at it or flank the creature.\n "
                        "Type 'charge' to fight head on or 'flank' to catch it by surprise.\n").lower()
        if choice3 == "charge":
            print("The goblin saw you coming and teleported away!\n Game Over!")
        else:
            choice4 = input("You have slain the goblin, but it threw the treasure behind one of three "
                            "doors before it died. There is a Red, Blue and Yellow door.\n Type the door color you want to go in to.\n").lower()
            if choice4 == "red":
                print("You entered a room lit aflame by the eternal fire. Your body has burned to a crisp!\n Game Over!")
            elif choice4 == "blue":
                print("You have been turned into a bat by the caves wizard.\n Game Over!")
            elif choice4 == "yellow":
                print("Congratulations! You have secured the treasure.\n You Win!")
            else:
                print("You have entered a spiraling room and lost your will to live!\n Game Over!")
    else:
        print("Your soul has been sucked by a wraith.\n Game Over!")
else:
    print("You fell into an inescapable pit.\n Game Over!")