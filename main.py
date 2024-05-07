# import stuff
# check if there is a config file. the config file will have the info on first run and other preferences
# initialize app window
# see if DB exist if not run the wizard
# wizard will get teacher name and basic info an then creates the tables
# show main frame

import database
from os import path

if path.exists("database.db") == False:
    print("There is no database. Creating one...")
    # db = Database()
    # db.firstRun()

if path.exists("database.db"):
    print("There is a sql database file. Accessing Database")
    # db = database.Database()
    # print(db.read('*', "teachers").fetchall())

