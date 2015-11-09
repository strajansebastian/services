import sys
sys.path.append("..")

from DbMongo.DbMongo import DbMongo

dbmongo = DbMongo("localhost", 27017, "airbnb_pinterest")

dbmongo.add("google_repetition", "Data")

print("End Done")
