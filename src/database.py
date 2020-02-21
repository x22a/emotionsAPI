from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from bson.json_util import dumps
from flask import Flask, request
import re

# Connect to the database
client = MongoClient("mongodb://localhost:27017")
database = client["emotionChat"]
userCol = database["users"]
chatCol = database["chats"]



@jsonErrorHandler
def createUser(username):
    if list(userCol.find({"name": username}, {"_id" : 1})) != []:                                           # Checks if the User exists
        userId = list(userCol.find({"name": username}, {"_id" : 1}))[0]['_id']                              # Returns the ID of the user
        return f"{username} already exists in the Database with ID: ({userId}). Please try another name"
    else:
        userInfo = {
            "name" : username                                                                               #.lower().capitalize() to return the first letter in capital letters
        }
        userCol.insert_one(userInfo)
        userId = list(userCol.find({"name": username}, {"_id" : 1}))[0]['_id']   
        return f"User {username} added to de Database with ID: ({userId})"

@jsonErrorHandler
def createChat():
    chatInfo = {'Users': {'user': 'id'},
 'Texts': {'msg1': {'name': 'juan', 'text': 'hola peña'},
  'msg2': {'name': 'pepe', 'text': 'que dise juan'},
  'msg3': {'name': 'xabi', 'text': 'aupa ahí'},
  'msg4': {'name': 'xabi', 'text': 'a las 7'},
  'msg5': {'name': 'guille', 'text': 'vamos a por cerve'},
  'msg6': {'name': 'patri', 'text': 'a las 7'},
  'msg7': {'name': 'xabi', 'text': 'a las 7'}}}
    chatCol.insert_one(chatInfo)
    return "OOK"