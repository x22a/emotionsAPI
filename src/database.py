from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from bson.json_util import dumps
from flask import Flask, request
import re
from bson.objectid import ObjectId

# Connect to the database
client = MongoClient("mongodb://localhost:27017")
database = client["emotionChat"]
userCol = database["users"]
chatCol = database["chats"]



@jsonErrorHandler
def createUser():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        username = request.form.get('username')
        if list(userCol.find({"name": username}, {"_id" : 1})) != []:                                           # Checks if the User exists
            userId = list(userCol.find({"name": username}, {"_id" : 1}))[0]['_id']                              # Returns the ID of the user
            return f"{username} already exists in the Database with ID: ({userId}). Please try another name"
        else:
            userInfo = {
                "name" : username                                                                               #.lower().capitalize() to return the first letter in capital letters
            }
            userCol.insert_one(userInfo)                                                                        # Inserts username to DB
            userId = list(userCol.find({"name": username}, {"_id" : 1}))[0]['_id']   
            return f"User {username} added to de Database with ID: ({userId})"

        return '''<h1>Chat created with id: {}</h1>'''.format("ID")
    # When there is a GET it returns this html to ask for an username                
    return '''<form method="POST">                                                                              
                  Username: <input type="text" name="username"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

    

@jsonErrorHandler
def createChat():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        usernames = request.form.get('usernames')
        usernames = usernames.split(",")
        exist = []
        dontExist = []
        toInsert = {"Users":{}}
        for userna in usernames:
            userna = userna.strip()
            if list(userCol.find({"name": userna}, {"_id" : 1})) == []:
                dontExist.append(userna)
            else:
                exist.append(userna)
        for userna in exist:
            toInsert["Users"][f"{userna}"] = list(userCol.find({"name": userna}, {"_id" : 1}))[0]
            
        chatCol.insert_one(toInsert)
        chatID = list(chatCol.find({}).sort([("_id", -1)]).limit(1))[0]["_id"]
        return '''<h1>Chat created with id: {}</h1>'''.format(chatID)

    return '''<form method="POST">
                  Usernames: <input type="text" name="usernames"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@jsonErrorHandler
def addUser(chat_id):
    if request.method == 'POST':  #this block is only entered when the form is submitted
        usernames = request.form.get('usernames')
        usernames = usernames.split(",")
        exist = []
        dontExist = []
        toUpdate = {"Users":{}}
        for userna in usernames:
            userna = userna.strip()
            if list(userCol.find({"name": userna}, {"_id" : 1})) == []:
                dontExist.append(userna)
            else:
                exist.append(userna)
        for userna in exist:
            toUpdate["Users"][f"{userna}"] = list(userCol.find({"name": userna}, {"_id" : 1}))[0]
            chatCol.update({"_id": ObjectId(chat_id)}, {"$set": {f"Users.{userna}" : list(userCol.find({"name": userna}, {"_id" : 1}))[0]}})
            
        
        return '''User added'''

    return '''<form method="POST">
                  Usernames: <input type="text" name="usernames"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''







"""    chatInfo = {'Users': {'user': 'id'},
 'Texts': {'msg1': {'name': 'juan', 'text': 'hola peña'},
  'msg2': {'name': 'pepe', 'text': 'que dise juan'},
  'msg3': {'name': 'xabi', 'text': 'aupa ahí'},
  'msg4': {'name': 'xabi', 'text': 'a las 7'},
  'msg5': {'name': 'guille', 'text': 'vamos a por cerve'},
  'msg6': {'name': 'patri', 'text': 'a las 7'},
  'msg7': {'name': 'xabi', 'text': 'a las 7'},
  'msg8': {'name': 'hector', 'text': 'aupa ahí'}}}"""