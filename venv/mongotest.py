from web import *

contacts = mongo.db.contacts.find()
print(contacts)

