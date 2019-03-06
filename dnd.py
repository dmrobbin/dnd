import random
from Character import *


def save_character(new_character):

    with open("{}.txt".format(new_character.name), "w+") as doc:
        print("Writing character to {}.txt".format(new_character.name))
        doc.write("{}\n".format(new_character.name))
        doc.write("{}\n".format(str(new_character.level)))
        doc.write("{}\n".format(new_character.race))
        doc.write("{}\n".format(new_character.cla))
        doc.write("{}\n".format(str(new_character.proficiency)))
        doc.write("{}\n".format(str(new_character.stats)))

        curr = 1
        while curr <= int(new_character.level):
            doc.write("{}-".format(str(curr)))
            doc.write("{}\n".format(str(new_character.features[curr])))
            curr += 1


def load_character():

    name = input(("Please enter character name\n"))

    with open("{}.txt".format(name)) as doc:
        doc.readline()
        level = int(doc.readline())
        race = doc.readline()
        cla = doc.readline()
        doc.readline()

        stats = doc.readline()

        #clean stat row into list
        cleaned_stats = stats.replace("{","")
        cleaned_stats = cleaned_stats.replace("}", "")
        cleaned_stats = cleaned_stats.replace(",", ":")
        cleaned_stats = cleaned_stats.replace("'", "")
        cleaned_stats = cleaned_stats.replace(" ", "")
        list_of_stats = cleaned_stats.split(":")

        #remove stat names

        # string fix testing!!!
        race = race.strip()
        cla = cla.strip()

        i = 0
        while i < 6:
            list_of_stats.pop(i)
            i += 1

        #convert stats
        i = 0
        while i<6:
            list_of_stats[i] = int(list_of_stats[i])
            i += 1

        if cla == 'Fighter':
            new_character = Fighter(race)
        elif cla == 'Wizard':
            new_character = Wizard(race)
        elif cla=='Rogue':
            new_character = Rogue(race)
        elif cla == "Barbarian":
            new_character = Barbarian(race)
        elif cla == "Bard":
            new_character = Bard(race)
        elif cla == "Cleric":
            new_character = Cleric(race)
        elif cla == "Druid":
            new_character = Druid(race)
        elif cla == "Monk":
            new_character = Monk(race)
        elif cla == "Paladin":
            new_character = Paladin(race)
        elif cla == "Ranger":
            new_character = Ranger(race)
        elif cla == "Sorcerer":
            new_character = Sorcerer(race)
        elif cla == "Warlock":
            new_character = Warlock(race)
        else:
            raise()

        new_character.name = name
        new_character.level = level

        new_character.stats['str'] = list_of_stats[0]
        new_character.stats['dex'] = list_of_stats[1]
        new_character.stats['con'] = list_of_stats[2]
        new_character.stats['int'] = list_of_stats[3]
        new_character.stats['wis'] = list_of_stats[4]
        new_character.stats['cha'] = list_of_stats[5]

        return new_character


#creator start
load = input("Would you like to load a previous character? yes or no?")

if load == 'no':

    name = input(str("What is the name of your character?"))

    lvl = input(str("What level is your character?"))

    # ensure valid race and class

    race = ''

    valid_R = 0
    while valid_R == 0:

        #c heck valid race name
        race = input(str("What race is your character, human ,elf, dwarf?, dragonborn, gnome, half-elf, halfling, half-orc, or tiefling"))
        if race == "human":
            valid_R += 1
        elif race == "elf":
            valid_R += 1
        elif race == "dwarf":
            valid_R += 1
        elif race == "dragonborn":
            valid_R += 1
        elif race == "gnome":
            valid_R += 1
        elif race == "half-elf":
            valid_R += 1
        elif race == "halfling":
            valid_R += 1
        elif race == "half-orc":
            valid_R += 1
        elif race == "tiefling":
            valid_R += 1
        elif race == "other":
            valid_R += 1
        else:
            print("Please enter a valid race name -\n")

    valid_C = 0
    while valid_C == 0:

        cls = input(str("What class is your character?\n"
                        "Barbarian, Bard, Cleric, Druid, Figther, Monk,"
                        "Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard"))

        # check valid class name
        if cls == "fighter":
            new_character = Fighter(race)
            valid_C += 1
        elif cls == "wizard":
            new_character = Wizard(race)
            valid_C += 1
        elif cls == "rogue":
            new_character= Rogue(race)
            valid_C += 1
        elif cls == "barbarian":
            new_character = Barbarian(race)
            valid_C += 1
        elif cls == "bard":
            new_character = Bard(race)
            valid_C += 1
        elif cls == "cleric":
            new_character = Cleric(race)
            valid_C += 1
        elif cls == "druid":
            new_character = Druid(race)
            valid_C += 1
        elif cls == "monk":
            new_character = Monk(race)
            valid_C += 1
        elif cls == "paladin":
            new_character = Paladin(race)
            valid_C += 1
        elif cls == "ranger":
            new_character = Ranger(race)
            valid_C += 1
        elif cls == "sorcerer":
            new_character = Sorcerer(race)
            valid_C += 1
        elif cls == "warlock":
            new_character = Warlock(race)
            valid_C += 1
        else:
            print("Please enter a valid class name -\n")

    new_character.name = name
    new_character.roll_stats()
    new_character.add_racial()

    curr = 0

    while curr < int(lvl):
        new_character.level_up()
        curr += 1

else:
    new_character = load_character()

run = 0

#control panel
while run == 0:
    sure = 0
    choice = (input("Press 1 to make an attack roll \n"
                   "press 2 to view your characters stats\n"
                   "press 3 to view your characters features\n"
                   "press 4 to change adjust your characters stats\n"
                   "press 5 to save your character as .txt\n"
                   "press 6 to load a previous character from .txt\n"
                   "press 7 to level up your character \n"
                    "press 8 to level down your character\n"
                    "press anything else to exit\n"))

    if choice == '1':
        new_character.attack()
    elif choice == '2':
        new_character.show_stats()
    elif choice == '3':
        print("Level {} {} \n".format(new_character.level,new_character.cla))
        new_character.class_features()
    elif choice == '4':
        new_character.adjust_stats()
    elif choice == '5':
        save_character(new_character)
    elif choice == '6':
        new_character = load_character()
    elif choice == '7':
        new_character.level_up()
    elif choice == '8':
        new_character.level_down()
    else:
        confirm=input("Are you sure that you want to quit? Type yes if you would like to quit.")
        if confirm == 'yes':
            run = 1

    print("\n")
