from datetime import datetime
import pymongo
from pymongo import MongoClient
from pymongo.collection import ReturnDocument
from Project.db.ConfigDB import *
from Project.Line.lineAPI import *
from Project.db.FindFunction import *


from bson.objectid import ObjectId


collection = db["tasks"]


# remove or cancel
def RejectTask(id):
    user = []
    result = FindTaskByID(id)
    taskQuery = {"_id":ObjectId(id)}
    setValue = { "$set": {"status":"Reject"}}
    collection.update_one(taskQuery,setValue)
    messageBack = {
                    "type": "text",
                    "text": "{}".format("@"+" @".join(result["member"])),
                    "weight": "bold",
                    "size": "md",
                    "color": "#F93636FF",
                    "align": "start",
                    "margin": "sm",
                    "contents": []
    }
    user.append(messageBack)

    return user



def ReviewTaskByID(taskId):
    result = FindTaskByID(taskId)
    taskQuery = {"_id":ObjectId(taskId)}
    setValue = { "$set": {"status":"Review"}}
    collection.update_one(taskQuery,setValue)
    
    return result

def AcceptTaskByID(id):
    result = FindTaskByID(id)
    taskQuery = {"_id":ObjectId(id)}
    setValue = { "$set": {"status":"Done","done_at":datetime.now()}}
    collection.update_one(taskQuery,setValue)
    
    return result

#Reject status to In Progress
def RejectTaskByID(id):
    result = FindTaskByID(id)
    taskQuery = {"_id":ObjectId(id)}
    setValue = { "$set": {"status":"In Progress"}}
    collection.update_one(taskQuery,setValue)
    
    
    return result