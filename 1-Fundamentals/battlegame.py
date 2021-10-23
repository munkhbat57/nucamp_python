game_on = True

while game_on:
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 200

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 120

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Orc")
        print("5)   Exit")
        character = input("Choose your character: ").lower()
        if character == '1' or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == '2' or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == '3' or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character == '4' or character == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break

        elif character == '5' or character == "exit":
            game_on = False
            break

        else:
            print("Unknown character")

    while game_on:
        print(
            f"Your chosen character is {character}, your hp is {my_hp}, your damage is {my_damage}")
        dragon_hp -= my_damage
        print(f"The {character} damaged the Dragon!\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle\n")
            decision = input("Do you want to play again? Y/n ").lower()
            if decision == 'y':
                game_on = True
            elif decision == 'n':
                game_on = False
            break
        my_hp -= dragon_damage
        print(f"{character} has been damaged and it's hp is {my_hp}\n")
        if my_hp <= 0:
            print(f"{character} has lost the battle\n")

            while True:
                decision = input("Do you want to play again? Y/n ").lower()
                if decision == 'y':
                    game_on = True
                    break
                elif decision == 'n':
                    game_on = False
                    break
                else:
                    continue

            break
