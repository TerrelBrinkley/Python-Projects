import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")

        choice = input("Enter your choice: ")
        if choice == "1":
            diceRollOne = random.randint(1, 6)
            diceRollTwo = random.randint(1, 6)

            sumOfDice = diceRollOne + diceRollTwo

            print("\nYou rolled a ...", diceRollOne)
            print("You rolled a ...", diceRollTwo, "\n")
            print("You have rolled a total of: ", sumOfDice, "\n")
            if sumOfDice > high_score:
                high_score = sumOfDice
                print("New High Score!\n")
            if sumOfDice == 12:
                print("You've maxed your score!\n")
        if choice == "2":
            print("Good Bye!")
            break


dice_game()
