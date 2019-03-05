import random

class Character:

    stats = {'str': 10,'dex': 10,'con': 10,'int': 10,'wis': 10,'cha': 10}
    mods ={1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16:
        3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 39: 10}

    level = 1
    features = {}
    proficiency = 2
    race=""
    cla =""
    name=""
    pass

    #create a Character object with specified race put
    #put racial bonuses in constructor
    def __init__(self, race):
        self.race = race
        self.roll_stats()
        self.add_racial(race)

        pass


    def roll_stats(self):
        list_of_stats=['str','dex','con','int','wis','cha']

        print("Let's start by rolling stats!\n")
        assigned=0


        #loop to end when all stats are assigned
        while assigned < 6:

        #print stats left to be assigned
            print ("You have still not assigned: ")
            for stat in list_of_stats:
                print (stat)

            stat = self.random_stat()

            chosen = str(input("Which stat would you like to assign this score?\n "))

            self.stats[chosen]=stat
            #show stat
            print("Your {} stat is {}".format(chosen, self.stats[chosen]))

            list_of_stats.remove(chosen)
            #increment counter
            assigned+=1

        print("Your total stat distributions is")

        self.show_stats()

        pass

    #rolls a random stat
    def random_stat(self):

        print ("You are rolling stats!\n")

        dice =[]

        #roll your 4 dice for stats
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        print ("The first dice you rolled was a {}, the second was {}, "
               "the third was {} and the fourth was {}\n".format(dice[0], dice[1], dice[2], dice[3]))

        dice.sort()
        print ("Only the 3 highest dice are used in stat generation so your "
               "{} roll has been discarded.\n".format(dice[0]))

        #drop the lowest dice
        dice.pop(0)

        score =0

        #add up die results
        for die in dice:
            score+=die
        print ("Your total score for this stat is {}\n".format(score))

        return score

    def add_racial(self):
        #adds racial bonuses to stats


        if(self.race=='human'):
            for stat in self.stats:
                self.stats[stat]+=1
        elif (self.race=='elf'):
            self.stats['dex']+=2
            self.stats['int']+=1
        elif(self.race=='dwarf'):
            self.stats['con']+=2
            self.stats['wis']+=1
        else:
            raise()

        pass

    def adjust_stats(self):

        stat = input("Which stat?")
        amount = input("by how much?")

        self.stats[stat] += int(amount)

        pass

    def level_up(self):
        if self.level<20:
            self.level += 1
        else:
            print("Character levels cannot exceed 20")

        self.calculate_proficency()
        #print("\nCongratulations you are now level {}! \n Here are all of your class features: \n".format(self.level))
        self.class_features()

        pass

    def level_down(self):
        if self.level > 1:
            self.level -= 1
        else:
            print("Character levels cannot be lower than 1")

        # print class features

    def calculate_proficency(self):

        if self.level >= 17:
            self.proficiency = 6
        elif self.level >= 12:
            self.proficiency = 5
        elif self.level >= 9:
            self.proficiency = 4
        elif self.level >= 5:
            self.proficiency = 3
        else:
            self.proficiency = 2

        pass

    def class_features(self):
        lvl = 1
        while lvl <= self.level:
            print (lvl, self.features[lvl])
            lvl += 1
        pass

    def show_stats(self):

        for stat in self.stats:
            print(stat, self.stats[stat])

        pass

    def attack(self):
        stat = str(input("What abilty does this attack use? "))

        roll = random.randint(1,20)

        prof = (bool(input("Are you profiient in this attack? Please answer True or False")))

        atk= 0

        if prof:
            atk=roll+self.proficiency+self.mods[self.stats[stat]]
        else:
            atk=roll+self.stats[stat]

        print ("your attack is {}".format(atk))
        pass

class Fighter(Character):

    features = {1: 'fighting style, second wind', 2: 'action surge', 3: 'Martial archetype',
                4: 'ability score improvement', 5: 'extra attack', 6: 'ability score improvement',
                7: "Martial archetype feature", 8: "Ability score improvement", 9: "Indomitable (One use)",
                10: "Martial archetype feature", 11: "Extra attack (two uses", 12: "Ability score improvement",
                13: "Indomitable (two uses", 14: "ability score improvement", 15: "Martial archetype feature",
                16: "Ability score improvement", 17: "Action surge (two uses), Indomitable (three uses",
                18: "Martial archetype feature", 19: "ablity score improvement", 20: "Extra attack (three uses"}


    def __init__(self, race):

        #self.roll_stats()
        self.race = race
        self.cla = "Fighter"


        pass

class Wizard(Character):

    features = {1: 'spell casting, arcane recovery', 2: 'arcane tradition', 3: '-',
                4: 'Ability score improvement', 5: '-', 6: 'arcane tradition feature', 7: "-",
                8: "Ability score improvement", 9: "-", 10: "arcane tradition feature", 11: "-",
                12: "Ability score improvement", 13: "-", 14: "Arcane tradition feature", 15: "-",
                16: "Ability score improvement", 17: "-", 18: "spell mastery",
                19: "ability score improvement", 20: "Signature spell"}

    def __init__(self, race):
        self.race = race
        self.cla = "Wizard"

    pass

class Rogue(Character):

    features = {1: 'Expertise, Sneak attack, Theives cant', 2: 'Cunning action', 3: 'Rougish archetype',
                4: 'Ability score improvement', 5: 'Unanny dodge', 6: 'Expertise', 7: "Evasion",
                8: "Ability score improvement", 9: "Rougish Archetype feature", 10: " Ability score improvement",
                11: "Reliable talent", 12: "Ability score improvement", 13: "Rougish archetype feature",
                14: "Blindsense", 15: "Slippery mind", 16: "Ability score improvement",
                17: "Rougish archetype feature", 18: "Elusive", 19: "Ability score improvement", 20: "Stroke of luck"}

    def __init__(self, race):
        self.race = race
        self.cla = "Rogue"

    pass

class Cleric(Character):
    features = {1: 'Spellcasting, Divine domain', 2: 'channel divinity 1/rest, Divine domain', 3: '-',
                4: 'Ablity score improvement', 5: 'Destory undead (CR 1/2)',
                6: 'Channel Divinity (2/rest), Divine Domain features', 7: "-",
                8: "Ability score improvement, Destory undead (CR 1), Divine domain features", 9: "-",
                10: "Divine intervention", 11: "Destroy undead (CR 2)", 12: "Ability score improvement",
                13: "-", 14: "Destroy Undead (CR 3)", 15: "-", 16: "Ability score improvement",
                17: "Destroy undead (CR4, Divine domain feature)", 18: "Channel Divinity (3/rest)",
                19: "Ability score improvement", 20: "Divine intervention improvement"}

    def __init__(self, race):
        self.race = race
        self.cla = "Cleric"

    pass


class Warlock(Character):
    features = {1: 'Otherworldly Patron, pact magic', 2: 'Eldritch invocations', 3: 'pact boon',
                4: 'Abilty score improvement', 5: '-', 6: 'Otherworldly patron feature', 7: "-",
                8: "Ability score improvment", 9: "-", 10: "otherwordly patron feature",
                11: "Mystic Arcanum (6th level)", 12: "Ability score improvement",
                13: "Mystica Arcanum (7th level)", 14: "otherworldy patron feature", 15: "Mystica arcanum (8th level)",
                16: "Ability score improvement", 17: "Mystic Arcanum (9th level)", 18: "-",
                19: "Ability score improvement", 20: "Eldritch master"}

    def __init__(self, race):
        self.race = race
        self.cla = "Warlock"

    pass


class Druid(Character):
    features = {1: 'Druidic, Spellcasting', 2: 'Wild Shape, Druid circle', 3: '-',
                4: 'Wild shape improvement, Ability score improvement', 5: '-', 6: 'Druid Circle feature', 7: "-",
                8: "Wild Shape improvement, ability score improvement", 9: "-", 10: "Druid Circle feature", 11: "-",
                12: "Abilty score improvement", 13: "-", 14: "Druid circle feature", 15: "-",
                16: "Ability score improvement", 17: "-", 18: "Timeless body, beast spells",
                19: "Ability score improvement", 20: "Archdruid"}

    def __init__(self, race):
        self.race = race
        self.cla = "Druid"

    pass


class Barbarian(Character):
    features = {1: 'Rage, Unarmored Defense', 2: 'Reckless attack ,danger sense', 3: 'Primal path',
                4: 'Ability score improvement', 5: 'Extra attack, fast movement', 6: 'path feature',
                7: "feral instinct", 8: "ability score improvement", 9: "barbarian critical (1 die)",
                10: "path feature", 11: "relentless", 12: "ability score improvement", 13: "brutal critical (2 dice)",
                14: "Path feature", 15: "persistent rage", 16: "ability score improvement",
                17: "Brutal critical (3 dice)", 18: "Indomitable might", 19: "Ability score improvement",
                20: "Primal champion"}

    def __init__(self, race):
        self.race = race
        self.cla = "Barbarian"

    pass


class Monk(Character):
    features = {1: 'unarmored defense, Martial arts', 2: 'Ki, unarmored movement',
                3: 'monastic tradition, deflect missiles', 4: 'Ability score improvement, slow fall',
                5: 'Extra attack, stunning strike', 6: 'ki-empowered strikes, monastic tradition feature',
                7: "Evasion, stillness of mind", 8: "Ability score improvement", 9: "Unarmored movement improvement",
                10: "purity of body", 11: "monastic tradition feature", 12: "ability score improvement",
                13: "Tongue of the sun and moon", 14: "Diamond soul", 15: "timeless body",
                16: "ability score improvement", 17: "monastic tradition feature", 18: "empty body",
                19: "Ability score improvement", 20: "perfect self"}

    def __init__(self, race):
        self.race = race
        self.cla = "Monk"

    pass


class Bard(Character):
    features = {1: 'Spellcasting, bardic inspiration (d6)', 2: 'Jack of all trades, Song of rest (d6)',
                3: 'Bard college, Expertise', 4: 'Ability score improvement',
                5: 'Bardic inspiration (d8), font of inspiration', 6: 'Countercharm, bard college feature', 7: "-",
                8: "ability score improvement", 9: "song of rest (d8)", 10: "Bardic inspiration (d10)", 11: "-",
                12: "ability score improvement", 13: "Song of rest (d10)", 14: "Magical secrets, Bard college feature",
                15: "Bardic inspiration (d12)", 16: "Ability score improvement", 17: "Song of rest (d12)",
                18: "Magical secrets", 19: "Ability score improvement", 20: "Superior inspiration"}

    def __init__(self, race):
        self.race = race
        self.cla = "Bard"

    pass


class Ranger(Character):
    features = {1: 'Facored enemy, natural explorere', 2: 'fighting style, spellcasting',
                3: 'primeval awareness, ranger conclave', 4: 'ability score improvement', 5: 'ranger conclave feature',
                6: 'greater favored enemy', 7: "ranger conclave feature",
                8: "ability score improvement, fleet of foot", 9: "-", 10: "hide in plain sight",
                11: "ranger conclave feature", 12: "ability score improvement", 13: "-", 14: "vanish",
                15: "ranger conclave feature", 16: "ability score improvement", 17: "-", 18: "feral senses",
                19: "ability score improvement", 20: "Foe slayer"}

    def __init__(self, race):
        self.race = race
        self.cla = "Ranger"

    pass


class Paladin(Character):
    features = {1: 'Divine sense, lay on hands', 2: 'Fighting style, spellcasting, divine smite',
                3: 'Divine health, sacred oath', 4: 'ability score improvement', 5: 'extra attack',
                6: 'Auro of protection', 7: "sacred oath feature", 8: "ability score improvement", 9: "-",
                10: "auro of courage", 11: "improved divine smite", 12: "Ability score improvement",
                13: "-", 14: "cleansing touch", 15: "sacred oath feature", 16: "ability score improvement",
                17: "-", 18: "aura improvements", 19: "ability score improvement", 20: "sacred oath feature"}

    def __init__(self, race):
        self.race = race
        self.cla = "Paladin"

    pass


class Sorcerer(Character):
    features = {1: 'spellcasting, sorcerous origin', 2: 'font of magic', 3: 'metamagic', 4: 'ability score improvent',
                5: '-', 6: 'sorcerous origin feature', 7: "-", 8: "ability score improvement", 9: "-", 10: "metamagic",
                11: "-", 12: "ability score improvement", 13: "-", 14: "sorcerous origin feature", 15: "-",
                16: "ability score improvement", 17: "metamagic", 18: "sorcerous origin feature",
                19: "ability score improvement", 20: "sorcerous restoration"}

    def __init__(self, race):
        self.race = race
        self.cla = "Sorcerer"

    pass

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
load = input("Would you like to load a previous character yes or no?")

if load == 'no':

    name = input(str("What is the name of your character?"))

    lvl = input(str("What level is your character?"))

    # ensure valid race and class

    race=''

    valid_R = 0
    while valid_R == 0:

        #c heck valid race name
        race = input(str("What race is your character, human ,elf, or dwarf?"))
        if race == "human":
            valid_R += 1
        elif race == "elf":
            valid_R += 1
        elif race == "dwarf":
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
