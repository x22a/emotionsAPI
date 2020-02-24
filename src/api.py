from flask import Flask
import os
from database import createUser, createChat, addUser, addMessage, listaChat
from sentiments import userSentiment, chatSentiment
from recomendations import userRecom
from landPage import landPage


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def landPages():
    return landPage()

@app.route("/user/create", methods=['GET', 'POST'])
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

@app.route('/chat/<chat_id>/list', methods=['GET', 'POST']) 
def listaChats(chat_id):
    return listaChat(chat_id)

@app.route('/chat/<chat_id>/sentiment', methods=['GET', 'POST'])
def chatSentiments(chat_id):
    return chatSentiment(chat_id)

@app.route('/user/<user>/sentiment', methods=['GET', 'POST'])
def getSentiments(user):
    return userSentiment(user)

@app.route('/user/<user>/recommend', methods=['GET', 'POST'])
def userRecommends(user):
    return userRecom(user)

app.run("0.0.0.0", os.getenv("PORT"), debug=True)

