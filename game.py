import random

def create_clones(number_of_clones):
    if number_of_clones <= 0:
        print("You cannot create zero or a negative number of shadow clones.")
    else:
        print(f"{number_of_clones} shadow clones have been created!")
        print("There are now enough clones. What do you want to do with them?")
        next_decision()

def next_decision():
    print("1. Train with the clones to improve your ninja skills.")
    print("2. Send the clones on a spy mission to a neighboring ninja village.")
    print("3. Disperse the clones and return to ninjutsu training.")

    choice = input("Choose option 1, 2, or 3: ")
    interpret_decision(choice)

def interpret_decision(choice):
    if choice == "1":
        print("You train with the clones to improve your ninja skills.")
        shuriken()
    elif choice == "2":
        print("You send the clones on a spy mission to a neighboring ninja village.")
        hokage()
    elif choice == "3":
        print("You disperse the clones and return to ninjutsu training.")
        chakra_nature()
    else:
        print("Invalid choice. Try again.")
        next_decision()

def shuriken():
    print("Learning a new skill: Shadow Shuriken!")
    print("During training with the clones, you improved your shadow shuriken-throwing skill.")
    duel()

def duel():
    print("After training, your friend from the Leaf Village, Naruto Uzumaki, challenges you to a duel.")
    print("Naruto may have had poor grades at the Ninja Academy, but you fear he might still surpass you. What will you do?")
    fight = input("Choose option 1 or 2: ")
    naruto_duel(fight)

def naruto_duel(fight):
    if fight == "1":
        print("You and Naruto face off in a duel. Naruto created many shadow clones, but you caught him off guard and won!")
        next_decision()
    elif fight == "2":
        print("Naruto laughs at you. You leave the training ground.")
        next_decision()
    else:
        print("Please choose a valid option.")
        duel()

def hokage():
    print("You enter the Hokage's office to present the information gathered by your clones during the mission.")
    print("The Hokage appreciates your efforts and promises a reward for the valuable information.")
    reward()

def reward():
    print("As a reward for the information, the Hokage offers advanced training, but his schedule is full due to village matters.")
    training_decision = input("Do you want to train in the village? (yes/no): ")
    if training_decision.lower() == "yes":
        print("You decided to train in the village. The Hokage finds time to train you personally.")
        village_training()
    else:
        print("You decided to return to training with the clones.")
        next_decision()

def village_training():
    print("You start advanced training in the village. The Hokage assigns you tasks to enhance your ninja skills.")
    tasks = ["Defeat a group of criminals", "Conduct a diplomatic mission", "Protect an important figure"]

    for task in tasks:
        print(f"Task: {task}")
        response = input("Will you complete this task? (yes/no): ")

        if response.lower() == "yes":
            print("Task completed! You gain new skills.")
            print("You now have better chakra control and improved shadow clone techniques.")
        else:
            print("Task failed. You need to put in more effort during training.")

    print("After successful training, the Hokage congratulates you on your progress.")
    next_decision()

def chakra_nature():
    print("During ninjutsu training, you focus on discovering the nature of your chakra.")
    print("You find out that your dominant chakra nature is Water. This is crucial information for future battles.")
    water_training()

def water_training():
    training_choice = input("Will you stay in your village to find a jonin with Water nature, or will you embark on a dangerous journey to the Land of Water? (Choose option 1 or 2): ")
    if training_choice == "1":
        print("You decided to stay in your village and seek a jonin.")
        jonin_training()
    elif training_choice == "2":
        print("You decided to embark on a dangerous journey to the Land of Water.")
        land_of_water()
    else:
        print("Invalid choice. Try again.")
        water_training()

def land_of_water():
    print("You arrive at the Hidden Mist Village. The journey was perilous, and the village is full of wary people watching you cautiously.")
    mist_training = input("You meet Mizukage, Mei Terumi. She has heard good things about you from the Hokage and is willing to train you in Water-style jutsu. Will you accept her training? (yes/no): ")
    if mist_training.lower() == "yes":
        print("Mizukage trains you in Water-style jutsu. You quickly master them under her guidance.")
        print("You learn three new Water-style jutsu: Water Tornado, Wave Surge, and Water Dragon Explosion.")
        next_decision()
    else:
        print("You declined the Mizukage's training and return to your village.")
        next_decision()

def jonin_training():
    jonin_training_decision = input("You meet Yamato, who has both Water and Earth chakra natures and uses Wood Style. Will you train under him? (yes/no): ")
    if jonin_training_decision.lower() == "yes":
        print("Yamato trains you in Water-style jutsu. The training is intense.")
        print("You master two new jutsu: Water Tornado and Wave Surge.")
        next_decision()
    elif jonin_training_decision.lower() == "no":
        print("You decide to leave the village and travel to the Land of Water.")
        land_of_water()
    else:
        print("Invalid choice. Try again.")
        jonin_training()

# Example of jutsu descriptions
jutsu = {
    "Shadow Clone": "Creates shadows to confuse the enemy.",
    "Water Style: Water Tornado": "Creates a powerful water tornado.",
    "Water Style: Wave Surge": "Sends waves toward the enemy.",
    "Water Style: Water Dragon Explosion": "Causes a water dragon explosion."
}

# Game storyline
print("Welcome, young ninja! You have come to learn the Shadow Clone technique.")
print("How many clones would you like to create? Enter a number:")
number_of_clones = int(input())
create_clones(number_of_clones)
