import time

def start_game():
    print("Welcome to the Fantasy Adventure Game!")
    input("Press Enter to begin...")
    print("\nYou are a brave adventurer on a quest to save the kingdom from an evil sorcerer.")
    time.sleep(2)
    print("As you journey through the mystical forest, you come across a mysterious crossroad.")
    time.sleep(2)
    decision_point_1()

def decision_point_1():
    print("\nAt the crossroad, you see three paths:")
    choice = input("1. The dark and ominous forest path\n2. The winding mountain trail\n3. The hidden cave entrance\n")
    if choice == "1":
        print("\nYou venture into the dark forest.")
        time.sleep(2)
        decision_point_2()
    elif choice == "2":
        print("\nYou decide to climb the winding mountain trail.")
        time.sleep(2)
        decision_point_3()
    elif choice == "3":
        print("\nYou enter the hidden cave.")
        time.sleep(2)
        decision_point_4()
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        decision_point_1()

def decision_point_2():
    print("\nIn the dark forest, you encounter a group of goblins.")
    choice = input("1. Attempt to fight them\n2. Sneak past them\n")
    if choice == "1":
        print("\nYou engage in a fierce battle with the goblins. After a hard-fought struggle, you emerge victorious.")
        time.sleep(2)
        decision_point_5()
    elif choice == "2":
        print("\nYou successfully sneak past the goblins and continue deeper into the forest.")
        time.sleep(2)
        decision_point_5()
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        decision_point_2()

def decision_point_3():
    print("\nYou reach the mountain's peak and find a majestic eagle.")
    choice = input("1. Ask the eagle for guidance\n2. Continue your journey without help\n")
    if choice == "1":
        print("\nThe eagle imparts its wisdom and guides you safely down the mountain.")
        time.sleep(2)
        decision_point_5()
    elif choice == "2":
        print("\nYou continue your journey alone but face challenges along the way.")
        time.sleep(2)
        decision_point_5()
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        decision_point_3()

def decision_point_4():
    print("\nInside the cave, you discover an old tome with magical incantations.")
    choice = input("1. Study the tome\n2. Leave the cave without taking the tome\n")
    if choice == "1":
        print("\nYou study the tome and gain magical powers.")
        time.sleep(2)
        decision_point_5()
    elif choice == "2":
        print("\nYou decide not to tamper with unknown magic and leave the cave.")
        time.sleep(2)
        decision_point_5()
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        decision_point_4()

def decision_point_5():
    print("\nYou've made it through your chosen path and reached the sorcerer's lair.")
    print("The fate of the kingdom depends on your next actions.")
    choice = input("1. Confront the sorcerer\n2. Try to negotiate with the sorcerer\n")
    if choice == "1":
        print("\nYou bravely confront the sorcerer and engage in a magical battle.")
        print("The battle is intense, but you eventually defeat the evil sorcerer and save the kingdom!")
    elif choice == "2":
        print("\nYou attempt to negotiate with the sorcerer, but he is too far gone to reason.")
        print("You are forced to engage in a magical battle, but in the end, you defeat the sorcerer and save the kingdom!")
    else:
        print("Invalid input. Please try again.")
        time.sleep(2)
        decision_point_5()
    print("\nCongratulations! You have completed your quest and saved the kingdom!")

if __name__ == "__main__":
    start_game()
