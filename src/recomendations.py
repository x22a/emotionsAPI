import re
import pandas as pd
import numpy as np

from pymongo import MongoClient
from errorHandler import jsonErrorHandler
from bson.json_util import dumps
from flask import Flask, request
from bson.objectid import ObjectId
from json import dumps as jdumps
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
from config import dbURL

client = MongoClient(dbURL)
database = client["emotionChat"]
userCol = database["users"]
chatCol = database["chats"]


@jsonErrorHandler
def userRecom(user):
    """
    Recommends an user to another based on what is written by those users
    """
    idLista = list(chatCol.find({},{"_id": 1}))
    userLista = list(userCol.find({}, {"_id": 0, "name": 1}))
    lista = {}
    for chat in idLista:
        exText = list(chatCol.find({"_id": ObjectId(chat["_id"])}).sort([("Texts", 1)]).limit(1))[0]["Texts"].keys()
        exText = list(exText)[-1]
        match = re.findall(r"[^msg][0-9]*" ,exText)
        lastText = int(match[0])
        for use in userLista:
            for e in range(1, lastText+1):
                try:
                    if use["name"] not in lista.keys():
                        lista[use["name"]] = list(chatCol.find({"$and": [{"_id": ObjectId(chat["_id"])}, {f"Texts.msg{e}.name": use["name"]}]}))[0]["Texts"][f"msg{e}"]["text"] + ". "
                    else:
                        lista[use["name"]] += list(chatCol.find({"$and": [{"_id": ObjectId(chat["_id"])}, {f"Texts.msg{e}.name": use["name"]}]}))[0]["Texts"][f"msg{e}"]["text"] + ". "
                except:
                    pass
    print(lista)
    docs = lista
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(docs.values())
    m = sparse_matrix.todense()
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=docs.keys())
    similarity_matrix = distance(df,df)
    sim_df = pd.DataFrame(similarity_matrix, columns=docs.keys(), index=docs.keys())
    np.fill_diagonal(sim_df.values, 0) # Remove diagonal max values and set those to 0
    return f"{user} is likely to be friends with {sim_df.idxmax()[user]}" 