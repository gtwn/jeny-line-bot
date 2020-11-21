from datetime import datetime
import pymongo
from pymongo import MongoClient
from pymongo.collection import ReturnDocument
from Project.db.ConfigDB import *
from Project.Line.lineAPI import *

collection = db["task"]

def RejectTask(message,memberIds,userID):
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
            setValue = { "$set": {"status":"Done"}}
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