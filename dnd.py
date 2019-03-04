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

        self.stats[stat] += amount

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
                4: 'ability score improvement', 5: 'extra attack', 6: 'ability score improvement'}


    def __init__(self, race):

        #self.roll_stats()
        self.race = race
        self.cla = "Fighter"
        '''
        self.roll_stats()
        self.add_racial(race)
        '''


        pass





class Wizard(Character):


    def __init__(self, race):
        self.race = race
        self.cla = "Wizard"
        '''
        self.roll_stats()
        self.add_racial(race)
        '''

    pass


def save_character(new_character):

    with open("{}.txt".format(new_character.name), "w+") as doc:
        print("Writing character to {}.txt".format(name))
        doc.write("{}\n".format(name))
        doc.write("{}\n".format(str(new_character.level)))
        doc.write("{}\n".format(new_character.race))
        doc.write("{}\n".format(new_character.cla))
        doc.write("{}\n".format(str(new_character.proficiency)))
        doc.write("{}\n".format(str(new_character.stats)))

        curr = 1
        while curr <= int(lvl):
            doc.write("{}-".format(str(curr)))
            doc.write("{}\n".format(str(new_character.features[curr])))
            curr += 1


def load_character():
    new_character = Character
    name = input(("Please enter character name\n"))

    with open("{}.txt".format(name)) as doc:
        name = doc.readline()
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
        cleaned_stats = cleaned_stats.replace("\n", "")
        list_of_stats = cleaned_stats.split(":")

        #remove stat names

        i = 0
        while i < 6:
            list_of_stats.pop(i)
            i += 1

        #convert stats
        i = 0
        while i<6:
            list_of_stats[i] = int(list_of_stats[i])
            i += 1

        if cla == 'Fighter\n':
            new_character = Fighter(race)
        elif cla == 'Wizard':
            new_character = Wizard(race)
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
    race = input(str("What race is your character, human or elf?"))
    cls = input(str("What class is your character, fighter or wizard?"))
    lvl = input(str("What level is your character?"))

    if cls=='wizard':
        if race == 'elf':
            new_character = Wizard('elf')
        else:
            new_character = Wizard('human')
    else:
        if race == 'elf':
            new_character = Fighter('elf')
        else:
            new_character = Fighter('human')

    new_character.name = name
    new_character.roll_stats()

    curr = 0

    while curr < int(lvl):
        new_character.level_up()
        curr += 1

else:
    new_character = load_character()

run = 0

#control panel
while run == 0:

    choice = (input("Press 1 to make an attack roll \n"
                   "press 2 to view your characters stats\n"
                   "press 3 to view your characters features\n"
                   "press 4 to change adjust your characters stats\n"
                   "press 5 to save your character\n"
                   "press 6 to load a previous character\n"
                   "press 7 to level up your character \n"
                   "press anything else to exit\n"))


    if choice == '1':
        new_character.attack()
    elif choice == '2':
        new_character.show_stats()
    elif choice == '3':
        print (new_character.cla)
        print (new_character.level)
        new_character.class_features()
    elif choice == '4':
        new_character.adjust_stats()
    elif choice == '5':
        save_character(new_character)
    elif choice == '6':
        new_character = load_character()
    elif choice == '7':
        new_character.level_up()
    else:
        run = 1

    print("\n")
