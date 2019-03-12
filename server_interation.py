#!/usr/bin/env python

#!/usr/bin/python3

import pymysql
from Character import *

def add_record(new_character):
    # Open database connection
    db = pymysql.connect(host='ls-83b76412cfb19ce97b259074e362e7e2605c6a71.cmkceejlkolu.us-west-2.rds.amazonaws.com',
                         user='dbmasteruser',
                         password='P>wL5SB-;?ak&]U]xin47ZOy+|1&xml7',
                         db='dbmaster')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Delete old record
    sql = "DELETE FROM 5E_CHAR WHERE NAME = '%s'" % (new_character.name)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO 5E_CHAR(NAME, \
       LEVEL, RACE, CLASS, STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE ,WISDOM, CHARISMA) \
       VALUES ('%s', '%d', '%s', '%s', %d, %d, %d, %d, %d, %d)" % \
       (new_character.name, new_character.level, new_character.race, new_character.cla, new_character.stats['str'], new_character.stats['dex'], new_character.stats['con'], new_character.stats['int'], new_character.stats['wis'], new_character.stats['cha'])
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # disconnect from server
    db.close()

def import_character():

    name = input(("Please enter character name\n"))

    db = pymysql.connect(host='ls-83b76412cfb19ce97b259074e362e7e2605c6a71.cmkceejlkolu.us-west-2.rds.amazonaws.com',
                         user='dbmasteruser',
                         password='P>wL5SB-;?ak&]U]xin47ZOy+|1&xml7',
                         db='dbmaster')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM 5E_CHAR \
          WHERE NAME = '%s'" % (name)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchone()

        cla = results[3]
        race = results[2]
        level = results[1]

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
            raise ()

        new_character.stats['str'] = results[4]
        new_character.stats['dex'] = results[5]
        new_character.stats['con'] = results[6]
        new_character.stats['int'] = results[7]
        new_character.stats['wis'] = results[8]
        new_character.stats['cha'] = results[9]

        new_character.name = name
        new_character.level = level

        return new_character

    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()

