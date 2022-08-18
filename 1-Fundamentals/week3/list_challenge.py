import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Press enter to pick a card, or Q plus enter to quit:")
    if choice == "Q":
        break
    else:
        card = random.choice(diamonds)
        chosenCard = diamonds.index(card)
        diamonds.pop(chosenCard)
        hand.append(card)
        print("Your hand: ", hand)
        print("Remaining cards: ", diamonds)

    if not diamonds:
        diamonds == []
        print("There are no more cards to pick from")
