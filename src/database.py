from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from bson.json_util import dumps
from flask import Flask, request
from bson.objectid import ObjectId
from json import dumps as jdumps
import re


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
        if exist == []:
            raise ValueError("There is no valid users, please go to '/user/create' to add a new user first")
        for userna in exist:
            toInsert["Users"][f"{userna}"] = list(userCol.find({"name": userna}, {"_id" : 1}))[0]
            
        chatCol.insert_one(toInsert)
        chatID = list(chatCol.find({}).sort([("_id", -1)]).limit(1))[0]["_id"] # It returns the ID of the last created chat
        return '''<h1>Chat created with id: {}</h1>'''.format(chatID)

    return '''<form method="POST">
                  Usernames: <input type="text" name="usernames"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@jsonErrorHandler
def addUser(chat_id): # FALTA AÑADIR: COMPROBAR SI EL USUARIO YA ESTÁ
    if request.method == 'POST':  #this block is only entered when the form is submitted
        username = request.form.get('usernames')
        username = username.split(",")
        exist = []
        dontExist = []
        for userna in username:
            userna = userna.strip()
            if list(userCol.find({"name": userna}, {"_id" : 1})) == []:
                dontExist.append(userna)
            else:
                exist.append(userna)
        if exist == []:
            raise ValueError("There is no valid users, please go to '/user/create' to add a new user first")
        for userna in exist:
            chatCol.update_one({"_id": ObjectId(chat_id)}, {"$set": {f"Users.{userna}" : list(userCol.find({"name": userna}, {"_id" : 1}))[0]}})
            
        
        return f"User {exist} added to chat: {chat_id}"

    return '''<form method="POST">
                  Username: <input type="text" name="username"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@jsonErrorHandler
def addMessage(chat_id):
    if request.method == 'POST':  #this block is only entered when the form is submitted
        username = request.form.get('user')
        message = request.form.get('message')
        exist = []
        dontExist = []
        if list(chatCol.find({f"Users.{username}._id": list(userCol.find({"name": f"{username}"}, {"_id" : 1}))[0]["_id"]}, {"_id" : 1})) == []:
            dontExist.append(username)
        else:
            exist.append(username)
        if exist == []:
            raise ValueError("The user is not in the chat, go to '/chat/<chat_id>/adduser' to add an user to this chat")
        try: # If there is no messages, the exception will set the first message to 1, else it will take the last message number
            exText = list(chatCol.find({"_id": ObjectId(chat_id)}).sort([("Texts", 1)]).limit(1))[0]["Texts"].keys()
            exText = list(exText)[-1] #hay que hacerlo con regex
            match = re.findall(r"[^msg][0-9]*" ,exText)                            #exText = list(exText)[-1]
            lastEl = int(match[0])
        except:
            lastEl = 0
        chatCol.update_one({"_id": ObjectId(chat_id)}, {"$set": {f"Texts.msg{lastEl+1}" : {'name': username, 'text': message}}})
        
        return f"Message added to chat: {chat_id}"

    return '''<form method="POST">
                  Who sends the message?: <input type="text" name="user"><br>
                  Message: <input type="text" name="message"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@jsonErrorHandler
def listaChat(chat_id):
    exText = list(chatCol.find({"_id": ObjectId(chat_id)}).sort([("Texts", 1)]).limit(1))[0]["Texts"].keys()
    exText = list(exText)[-1]
    match = re.findall(r"[^msg][0-9]*" ,exText)
    lastText = int(match[0])
    lista = []
    for e in range(1, lastText+1):
        try:
            lista.append((list(chatCol.find({'_id': ObjectId(chat_id)}, {f"Texts.msg{e}.name"}))[0]["Texts"][f"msg{e}"]["name"], list(chatCol.find({'_id': ObjectId(chat_id)}, {f"Texts.msg{e}.text"}))[0]["Texts"][f"msg{e}"]["text"]))
        except:
            pass
    print(lista)
    return jdumps(lista)




