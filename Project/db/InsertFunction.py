from datetime import datetime
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *
from Project.Line.lineAPI import *


collection = db["task"]

## เพิ่มงาน
def InsertTask(message,userProfile,userID,groupID,memberIds):
    nameTag = ''
    tagCount = message.count('@')
    task = message.lower().split("#task ")[1].split("#")[0]
    if '#by' not in message.lower() :
        by = 'To night'
    else :
        by = message.lower().split("#by ")[1].split()[0]
    by += '/2020'
    ts =  int(datetime.strptime(by,"%d/%m/%Y").timestamp())
    dt = (datetime.fromtimestamp(int(ts))).strftime('%Y-%m-%d %H:%M:%S')
    dtObj =  datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    # for i in range (tagCount) :
    #     if i+1 == tagCount:
    #         tag = message.split('@')[i+1].split(' ')[0]
    #     else:
    #         tag = message.split('@')[i+1]
    #     nameTag += tag + ' '
    #     data = {"order_to":tag,
    #             "task":task,
    #             "deadline":dtObj,
    #             "created_at":datetime.now(),
    #             "done_at":datetime.min,
    #             "order_by":userProfile,
    #             "from_id":userID,
    #             "group_id":groupID,
    #             "status":"In Progress"}

    #     collection.insert_one(data)
    for uid in memberIds['memberIds']:
        display = GetUserProfile(uid,Channel_Access_Token)
        if display in message:
            nameTag += display + ' '
            data = {"order_to":display,
                    "task":task,
                    "deadline":dtObj,
                    "created_at":datetime.now(),
                    "done_at":datetime.min,
                    "order_by":userProfile,
                    "from_id":userID,
                    "order_id":uid,
                    "group_id":groupID,
                    "status":"In Progress"}

            collection.insert_one(data)
    

    return nameTag,task,by
