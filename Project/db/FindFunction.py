from datetime import datetime
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *

collection = db["task"]

## งานที่ต้องทำ
def FindTask(userID):
    reply = []
    # results = collection.find({"order_to":userProfile},{"_id":0,"order_to":0,"task":1,"deadline":1,"created_at":1,"order_by":1,"done_at":0})
    results = collection.find({"order_id":userID,"status":"In Progress"})
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
        else:
            status = 'ยังไม่เลยกำหนด'
        messageBack = {"type":"text",
                    "text":"งาน : {}\nกำหนดส่ง : {}\nสั่งโดย : {}\nตั้งแต่วันที่ : {}\nสถานะ : {}".format(result["task"],deadline,result["order_by"],createAt,status)
                    }
        reply.append(messageBack)
    return reply

## งานที่สั่ง
def FindFollowTask(userID):
    reply = [] 
    results = collection.find({"from_id":userID, "status":"In Progress"})
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
        else:
            status = 'ยังไม่เลยกำหนด'
        messageBack = {"type":"text",
                    "text":"งาน : {}\nกำหนดส่ง : {}\nสั่งโดย : {}\nตั้งแต่วันที่ : {}\nสถานะ : {}".format(result["task"],deadline,result["order_by"],createAt,status)
                    }
        reply.append(messageBack)
    return reply