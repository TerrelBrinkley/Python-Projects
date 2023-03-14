wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print('Select a Character')
    print("Wizard")
    print("Elf")
    print("Human")
    character = input('Choose your character:').lower()

    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("That is not a valid option")

print(character)
print(my_hp)
print(my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragons hitpoints are now: ", dragon_hp)

    if(dragon_hp <= 0):
        print("The Dragon has lost the battle")
        break

    my_hp -= dragon_damage
    print("The Dragon strikes back at ", character, "!")
    print("The", character, "hitpoints are now: ", my_hp)

    if(my_hp < 0):
        print("The ", character, "has lost the battle!")
        break
