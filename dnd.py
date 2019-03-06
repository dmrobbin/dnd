import random
import json
import time
from Character import *


def save_character(new_character):

    file_type = input("Would you like to save as txt or json")

    if file_type == 'txt':

        with open("{}.txt".format(new_character.name), "w+") as doc:
            print("Writing character to {}.txt\n...\n".format(new_character.name))
            doc.write("{}\n".format(new_character.name))
            doc.write("{}\n".format(str(new_character.level)))
            doc.write("{}\n".format(new_character.race))
            doc.write("{}\n".format(new_character.cla))
            doc.write("{}\n".format(str(new_character.proficiency)))
            doc.write("{}\n".format(str(new_character.stats)))
            doc.write("{}\n".format(str(new_character.notes)))

            curr = 1
            while curr <= int(new_character.level):
                doc.write("{}-".format(str(curr)))
                doc.write("{}\n".format(str(new_character.features[curr])))
                curr += 1

    else:
        print("Writing character to {}json.txt\n...\n".format(new_character.name))
        data = {'name': new_character.name, 'level': new_character.level, 'race': new_character.race,
                'class': new_character.cla, 'proficiency': new_character.proficiency, 'stats': new_character.stats,
                'notes': new_character.notes}

        with open("{}json.txt".format(new_character.name), "w+") as doc:
            json.dump(data, doc)

    time.sleep(1)

def load_character():

    file_type = input("Would you like to load a txt or json file?\n")

    name = input(("Please enter character name\n"))

    if file_type == 'txt':

        with open("{}.txt".format(name)) as doc:
            doc.readline()
            level = int(doc.readline())
            race = doc.readline()
            cla = doc.readline()
            doc.readline()

            stats = doc.readline()
            notes = doc.readline()

            # clean stat row into list
            cleaned_stats = stats.replace("{","")
            cleaned_stats = cleaned_stats.replace("}", "")
            cleaned_stats = cleaned_stats.replace(",", ":")
            cleaned_stats = cleaned_stats.replace("'", "")
            cleaned_stats = cleaned_stats.replace(" ", "")
            list_of_stats = cleaned_stats.split(":")

            #clean notes row into list
            cleaned_notes = notes.replace("[", "")
            cleaned_notes = cleaned_notes.replace("]", "")
            cleaned_notes = cleaned_notes.replace("\n", "")
            cleaned_notes = cleaned_notes.replace("'", "")
            cleaned_notes = cleaned_notes.replace(",", ":")
            cleaned_notes = cleaned_notes.replace(" ", "")
            list_of_notes = cleaned_notes.split(":")

            # string cleaning

            race = race.strip()
            cla = cla.strip()

            # remove stat names

            i = 0
            while i < 6:
                list_of_stats.pop(i)
                i += 1

            # convert stats

            i = 0
            while i < 6:
                list_of_stats[i] = int(list_of_stats[i])
                i += 1

            if cla == 'Fighter':
                new_character = Fighter(race)
            elif cla == 'Wizard':
                new_character = Wizard(race)
            elif cla == 'Rogue':
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

            new_character.notes = list_of_notes

            time.sleep(0.5)
            print("\nLoaded successfully! \n")
            return new_character

    else:
        with open("{}json.txt".format(name)) as doc:
            data = json.load(doc)

            if data['class'] == 'Fighter':
                new_character = Fighter(data['race'])
            elif data['class'] == 'Wizard':
                new_character = Wizard(data['race'])
            elif data['class'] == 'Rogue':
                new_character = Rogue(data['race'])
            elif data['class'] == "Barbarian":
                new_character = Barbarian(data['race'])
            elif data['class'] == "Bard":
                new_character = Bard(data['race'])
            elif data['class'] == "Cleric":
                new_character = Cleric(data['race'])
            elif data['class'] == "Druid":
                new_character = Druid(data['race'])
            elif data['class'] == "Monk":
                new_character = Monk(data['race'])
            elif data['class'] == "Paladin":
                new_character = Paladin(data['race'])
            elif data['class'] == "Ranger":
                new_character = Ranger(data['race'])
            elif data['class'] == "Sorcerer":
                new_character = Sorcerer(data['race'])
            elif data['class'] == "Warlock":
                new_character = Warlock(data['race'])
            else:
                raise ()

            new_character.stats = data['stats']

            new_character.name = data['name']
            new_character.level = data['level']
            new_character.notes = data['notes']

            time.sleep(0.5)
            print("\nLoaded successfully! \n")
            return new_character



load = input("Would you like to load a previous character? yes or no?\n")

if load == 'no':

    # Build new character

    name = input(str("What is the name of your character?\n"))

    lvl = input(str("What level is your character?\n"))

    # ensure valid race and class

    race = ''

    valid_R = 0
    while valid_R == 0:

        #check valid race name

        race = input(str("What race is your character? human ,elf, dwarf, "
                         "dragonborn, gnome, half-elf, halfling, half-orc, or tiefling\n"))

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
                        "Barbarian, Bard, Cleric, Druid, Fighter, Monk,"
                        "Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard\n"))

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

    for x in range(int(lvl)-1):
        new_character.level_up()

# Load character from txt

else:
    new_character = load_character()

run = 0

# Main method

while run == 0:

    choice = (input("Press 1 to make an attack roll \n"
                    "press 2 to view your characters stats\n"
                    "press 3 to view your characters features\n"
                    "press 4 to change adjust your characters stats\n"
                    "press 5 to save your character as\n"
                    "press 6 to load a previous character from\n"
                    "press 7 to level up your character \n"
                    "press 8 to level down your character\n"
                    "press 9 to edit your notes\n"
                    "press 10 to view your notes\n"
                    "press 11 to view your spell casting info\n"
                    "press 12 to view your class resource\n"
                    "press anything else to exit\n"))

    if choice == '1':
        new_character.attack()
    elif choice == '2':
        new_character.show_stats()
    elif choice == '3':
        print("Level {} {} \n".format(new_character.level, new_character.cla))
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
    elif choice == '9':
        new_character.edit_notes()
    elif choice == '10':
        for i in range(len(new_character.notes)):
            print(i, "{} \n".format(new_character.notes[i]))
    elif choice == '11':
        if new_character.cla == 'Bard' or new_character.cla == 'Cleric' or new_character.cla == 'Druid' or new_character.cla == 'Paladin' or new_character.cla == 'Ranger' or new_character.cla == 'Sorcerer' or new_character.cla == 'Warlock' or new_character.cla == 'Wizard':
                new_character.caster_info()
        else:
                print("You are not a spell casting class.")
    elif choice == '12':
        new_character.class_resources()
    else:
        confirm = input("Are you sure that you want to quit? Type yes if you would like to quit.\n")
        if confirm == 'yes':
            run = 1

    print("\n")
