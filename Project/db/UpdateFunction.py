from datetime import datetime
import pymongo
from pymongo import MongoClient
from pymongo.collection import ReturnDocument
from Project.db.ConfigDB import *
from Project.Line.lineAPI import *
from Project.db.FindFunction import *


from bson.objectid import ObjectId


collection = db["tasklist"]

# remove or cancel
def RejectTaskInGroup(message,memberIds,userID):
    tagCount = message.count('@')
    count = 0
    task = message.split("#ยกเลิกงาน ")[1].split("@")[0]
    print(task)
    user = []
    for uid in memberIds['memberIds']:
        display = GetUserProfile(uid,Channel_Access_Token)

        if display in message:
            print(uid)
            print("task:"+task.strip())
            taskQuery = {"task":task.strip(),"order_id":uid,"from_id":userID}
            setValue = { "$set": {"status":"Reject","done_at":datetime.now()}}
            # sort = [('creation_date', pymongo.ASCENDING)]
            # updated_doc = collection.find_one_and_update(taskQuery, setValue,sort=sort,
            #                 return_document=ReturnDocument.AFTER)
            # print(updated_doc)
            collection.update_many(taskQuery,setValue)
            count += 1
            messageBack = {
                            "type": "text",
                            "text": "@"+display,
                            "weight": "bold",
                            "size": "md",
                            "color": "#F93636FF",
                            "align": "start",
                            "margin": "sm",
                            "contents": []
            }
            user.append(messageBack)
        if count == tagCount:
            break

    return task,user


# remove or cancel
def RejectTask(id):
    user = []
    result = FindTaskByID(id)
    taskQuery = {"_id":ObjectId(id)}
    setValue = { "$set": {"status":"Reject"}}
    collection.update_one(taskQuery,setValue)
    messageBack = {
                    "type": "text",
                    "text": "@"+result["order_to"],
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