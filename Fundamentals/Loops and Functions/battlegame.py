"""A simple text-based battle game where players fight a dragon."""

WIZARD = "Wizard"
ELF = "Elf"
HUMAN = "Human"

WIZARD_HP = 70
ELF_HP = 100
HUMAN_HP = 150

WIZARD_DAMAGE = 150
ELF_DAMAGE = 100
HUMAN_DAMAGE = 20

DRAGON_HP = 300
DRAGON_DAMAGE = 50

while True:
    print('Select a Character')
    print("Wizard")
    print("Elf")
    print("Human")
    chosen_character = input('Choose your character:').lower()

    if chosen_character == "1" or chosen_character == "wizard":
        chosen_character = WIZARD
        current_hp = WIZARD_HP
        damage_dealt = WIZARD_DAMAGE
        break
    elif chosen_character == "2" or chosen_character == "elf":
        chosen_character = ELF
        current_hp = ELF_HP
        damage_dealt = ELF_DAMAGE
        break
    elif chosen_character == "3" or chosen_character == "human":
        chosen_character = HUMAN
        current_hp = HUMAN_HP
        damage_dealt = HUMAN_DAMAGE
        break
    else:
        print("That is not a valid option")

print(chosen_character)
print(current_hp)
print(damage_dealt)

while True:
    DRAGON_HP -= damage_dealt
    print("The", chosen_character, "damaged the Dragon!")
    print("The Dragons hitpoints are now: ", DRAGON_HP)

    if DRAGON_HP <= 0:
        print("The Dragon has lost the battle")
        break

    current_hp -= DRAGON_DAMAGE
    print("The Dragon strikes back at ", chosen_character, "!")
    print("The", chosen_character, "hitpoints are now: ", current_hp)

    if current_hp < 0:
        print("The ", chosen_character, "has lost the battle!")
        break
