from flask import Flask, request, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
col = db.contacts


app = Flask(__name__, template_folder='templates/')
mongo = PyMongo(app)



@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/db')
def db():
    contacts = col.find()
    array = []
    for con in contacts:
        array.append(con)
    return render_template('db.html', contacts=array)

#   num = str(contacts.count())
#   return num
#    return render_template('db.html', contacts=contacts)
#    array = []
#   for con in contacts:
#      array.append(con)


if __name__ == "__main__":
    app.run()



