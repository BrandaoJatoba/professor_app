# import stuff
# check if there is a config file. the config file will have the info on first run and other preferences
# initialize app window
# see if DB exist if not run the wizard
# wizard will get teacher name and basic info an then creates the tables
# show main frame

from DB.database import *
import View

db = Database()
print(db.read('*', "teachers").fetchall())