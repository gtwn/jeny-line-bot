from flask import Flask ,  request, abort
from Project.Line.lineAPI import *
import requests
import json
from datetime import datetime
from Project.Config import *

import pymongo
from pymongo import MongoClient
from Project.Config import *


uri = "mongodb+srv://{}:{}@cluster0-aarl2.mongodb.net/{}?retryWrites=true&w=majority".format(DB_Username,DB_Password,DB_Name)
cluster = pymongo.MongoClient(uri)

db = cluster["{}".format(DB_Name)]

collection = db["task"]




app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello' , 200

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST' :
        payload = request.json 
        print('payload: ', payload)
        replyToken = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        sourceType = payload['events'][0]['source']['type']
        userID = payload['events'][0]['source']['userId']

        if sourceType == 'group' :
            groupID = payload['events'][0]['source']['groupId']
        else:
            groupID = ' '
        if 'Hi' in message :
            
            replyMessage = 'Say Hi from ' + userID + 'in groupID' + groupID
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        # if 'ข้อมูลกลุ่ม' in message :
        #     replyMessage = 'ข้อมูลกลุ่ม : {}'.format(GetGroupSummary(groupID,Channel_Access_Token))
        #     ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        # if 'สมาชิกกลุ่ม' in message : 
        #     replyMessage = 'สมาชิก ID : {}'.format(GetMemberUserIDs(groupID,Channel_Access_Token))
        #     ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'jeny' in message.lower() and '#order' in message.lower():
            profile = GetUserProfile(userID,Channel_Access_Token)
            orderTo,task,by = InsertTask(message,profile,userID,groupID)
            replyMessage = 'สั่งงานคุณ: {}\nรายละเอียดงาน: {}\nกำหนดส่ง: {}\nสั่งโดย: {}'.format(orderTo,task,by,profile)
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'jeny' in message and 'คำแนะนำ' in message:
            replyMsg = 'คำสั่งแนะนำ\n ต้องการสั่งงาน:\n Jeny #Order @... #Task .... #By date/month\n ต้องการดูงานที่ต้องทำ: #งานที่ต้องทำ\n ต้องการดูงานที่สั่ง: #งานที่สั่ง'
            ReplyMessage(replyToken,replyMsg,Channel_Access_Token)
        if 'jeny' in message.lower() and '#งานที่ต้องส่ง' in message or '#งานที่ต้องทำ' in message :
            profile = GetUserProfile(userID,Channel_Access_Token)
            ReplyTaskMessage(replyToken,FindTask(profile),Channel_Access_Token)
        if 'jeny' in message.lower() and '#งานที่สั่ง' in message :
            profile = GetUserProfile(userID,Channel_Access_Token)
            ReplyTaskMessage(replyToken,FindFollowTask(profile),Channel_Access_Token)
        else :
            ReplyTaskMessage(replyToken,'คำสั่งแนะนำ\n ต้องการสั่งงาน:\n Jeny #Order @... #Task .... #By date/month\n ต้องการดูงานที่ต้องทำ: #งานที่ต้องทำ\n',Channel_Access_Token)
        return request.json,200
        
    elif request.method == 'GET' :
        return 'this is method GET', 200

    else:
        abort(400)

## งานที่ต้องทำ
def FindTask(userProfile):
    reply = []
    # results = collection.find({"order_to":userProfile},{"_id":0,"order_to":0,"task":1,"deadline":1,"created_at":1,"order_by":1,"done_at":0})
    results = collection.find({"order_to":userProfile,"status":"In Progress"})
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
def FindFollowTask(userProfile):
    reply = [] 
    results = collection.find({"order_by":userProfile, "status":"In Progress"})
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

## เพิ่มงาน
def InsertTask(message,userProfile,userID,groupID):
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
    for i in range (tagCount) :
        if i+1 == tagCount:
            tag = message.split('@')[i+1].split(' ')[0]
        else:
            tag = message.split('@')[i+1]
        nameTag += tag + ' '
        data = {"order_to":tag,
                "task":task,
                "deadline":dtObj,
                "created_at":datetime.now(),
                "done_at":datetime.min,
                "order_by":userProfile,
                "from_id":userID,
                "group_id":groupID,
                "status":"In Progress"}

        collection.insert_one(data)

    return nameTag,task,by
