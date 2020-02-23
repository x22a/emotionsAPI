from flask import Flask
from database import createUser, createChat, addUser, addMessage

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

@app.route('/chat/<chat_id>/addmessage', methods=['GET', 'POST']) 
def addMessages(chat_id):
    return addMessage(chat_id)



app.run("0.0.0.0", 5000, debug=True)

