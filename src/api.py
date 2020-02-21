from flask import Flask, request
from database import createUser, createChat

app = Flask(__name__)


@app.route("/user/create/<username>")
def createUsername(username):
    return createUser(username)

@app.route('/chat/create') 
def createChats():
    return createChat()




app.run("0.0.0.0", 5000, debug=True)

