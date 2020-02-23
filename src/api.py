from flask import Flask, request
from database import createUser, createChat, addUser

app = Flask(__name__)


@app.route("/user/create/", methods=['GET', 'POST'])
def createUsername():
    return createUser()

@app.route('/chat/create', methods=['GET', 'POST']) 
def createChats():
    return createChat()

@app.route('/chat/<chat_id>/adduser', methods=['GET', 'POST']) 
def addUsers(chat_id):
    return addUser(chat_id)



app.run("0.0.0.0", 5000, debug=True)

