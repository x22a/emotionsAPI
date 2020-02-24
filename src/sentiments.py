from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from json import dumps as jdumps
from flask import Flask, request
from bson.objectid import ObjectId
import re
from config import dbURL

client = MongoClient(dbURL)
database = client["emotionChat"]
userCol = database["users"]
chatCol = database["chats"]


@jsonErrorHandler
def chatSentiment(chat_id):
    """
    Returns the emotion index of a given chat
    """
    exText = list(chatCol.find({"_id": ObjectId(chat_id)}).sort([("Texts", 1)]).limit(1))[0]["Texts"].keys()
    exText = list(exText)[-1]
    match = re.findall(r"[^msg][0-9]*" ,exText)
    lastText = int(match[0])
    lista = []
    for e in range(1, lastText+1):
        try:
            lista.append(list(chatCol.find({'_id': ObjectId(chat_id)}, {f"Texts.msg{e}.text"}))[0]["Texts"][f"msg{e}"]["text"])
        except:
            pass
    sia = SentimentIntensityAnalyzer()
    chatPol = sia.polarity_scores(" ".join(lista))
    negativity, positivity, compound = chatPol["neg"], chatPol["pos"], chatPol["compound"]
    totaSentiment = "This chat has a negativity of: " + str(negativity) + " A positivity of: " + str(positivity) + " With a total compound of: " + str(compound)
    return jdumps(totaSentiment)

@jsonErrorHandler
def userSentiment(user):
    """
    Returns the emotion index of a given User
    """
    sia = SentimentIntensityAnalyzer()
    idLista = list(chatCol.find({}, {"_id": 1}))
    lista = []
    for chat in idLista:
        exText = list(chatCol.find({"_id": ObjectId(chat["_id"])}).sort([("Texts", 1)]).limit(1))[0]["Texts"].keys()
        exText = list(exText)[-1]
        match = re.findall(r"[^msg][0-9]*" ,exText)
        lastText = int(match[0])

        for e in range(1, lastText+1):
            try:
                lista.append(list(chatCol.find({"$and": [{"_id": ObjectId(chat["_id"])}, {f"Texts.msg{e}.name": user}]}))[0]["Texts"][f"msg{e}"]["text"])
            except:
                pass
    chatPol = sia.polarity_scores(" ".join(lista))
    negativity, positivity, compound = chatPol["neg"], chatPol["pos"], chatPol["compound"]
    totaSentiment = f"{user} has a negativity of: " + str(negativity) + " A positivity of: " + str(positivity) + " With a total compound of: " + str(compound)
    return jdumps(totaSentiment)