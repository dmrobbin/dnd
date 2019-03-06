import random

class Character:

    stats = {'str': 10,'dex': 10,'con': 10,'int': 10,'wis': 10,'cha': 10}
    mods = {1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16:
        3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 39: 10}

    racial_traits = {}

    level = 1
    features = {}
    proficiency = 2
    race = ""
    cla = ""
    name = ""
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
        stats =[]
        for x in list_of_stats:
            stats.append(self.random_stat())

        print("you have rolled {} \n".format(stats))
        for stat in stats:
            good = 0
            while good == 0:
                print("{}\n".format(stat))
                chosen = str(input("Which stat would you like to assign this score?\n "))
                if chosen == "str":
                    self.stats[chosen] = stat
                    good +=1
                elif chosen == "dex":
                    self.stats[chosen] = stat
                    good += 1
                elif chosen == "con":
                    self.stats[chosen] = stat
                    good += 1
                elif chosen == "int":
                    self.stats[chosen] = stat
                    good += 1
                elif chosen == "wis":
                    self.stats[chosen] = stat
                    good += 1
                elif chosen == "cha":
                    self.stats[chosen] = stat
                    good += 1
                else:
                    print("\nPlease enter a valid stat name: str, con, dex, int, wis, cha \n")

        print("Your total stat distributions is\n")

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
            score += die
        print ("Your total score for this stat is {}\n".format(score))

        return score

    def add_racial(self):
        #adds racial bonuses to stats

        if self.race == 'human':
            for stat in self.stats:
                self.stats[stat] += 1
        elif self.race == 'elf':
            self.stats['dex'] += 2
        elif self.race == 'dwarf':
            self.stats['con'] += 2
        elif self.race == 'gnome':
            self.stats['int'] += 2
        elif self.race == 'halfling':
            self.stats['dex'] += 2
        elif self.race == 'half-orc':
            self.stats['str'] += 2
            self.stats['con'] += 1
        elif self.race == 'tiefling':
            self.stats['cha'] += 2
            self.stats['int'] += 1
        elif self.race == 'dwarf':
            self.stats['con'] += 2
        elif self.race == 'dragonborn':
            self.stats['str'] += 2
            self.stats['cha'] += 1
        elif self.race == 'half-elf':
            self.stats['cha'] += 2
            chosen = input("Choose the first stat for your half-elf racial +1 bonus")
            self.stats[chosen] += 1
            chosen = input("Choose the second stat for your half-elf racial +1 bonus")
            self.stats[chosen] += 1
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
            print(lvl, self.features[lvl])
            print("\n")
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

        if prof:
            atk = roll+self.proficiency+self.mods[self.stats[stat]]
        else:
            atk = roll+self.stats[stat]

        print("your attack is {}".format(atk))
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