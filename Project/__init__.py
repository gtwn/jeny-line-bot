from flask import Flask ,  request, abort
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

def GetGroupSummary(GroupID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/group/{}/summary'.format(GroupID)
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    resp = requests.get(api,headers=headers)
    return resp.text

def GetMemberUserIDs(GroupID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/group/{}/members/ids'.format(GroupID)
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    resp = requests.get(api,headers=headers)
    return resp.text

def GetUserProfile(userID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/profile/{}'.format(userID)
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    resp = requests.get(api,headers=headers)
    jsLoads = json.loads(resp.text)
    print("jsLoads:",jsLoads)
    return jsLoads["displayName"]

def GetGroupUserProfile(userID,GroupID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/group/{}/member/{}'.format(GroupID,userID)
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    resp = requests.get(api,headers=headers)
    jsLoads = json.loads(resp.text)
    return jsLoads["displayName"]

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
        if sourceType == 'group' :
            groupID = payload['events'][0]['source']['groupId']
        else:
            groupID = ' '
        if 'Hi' in message :
            userID = payload['events'][0]['source']['userId']
            replyMessage = 'Say Hi from ' + userID + 'in groupID' + groupID
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'ข้อมูลกลุ่ม' in message :
            replyMessage = 'ข้อมูลกลุ่ม : {}'.format(GetGroupSummary(groupID,Channel_Access_Token))
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'สมาชิกกลุ่ม' in message : 
            replyMessage = 'สมาชิก ID : {}'.format(GetMemberUserIDs(groupID,Channel_Access_Token))
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'jeny' in message.lower() and '#order' in message.lower():
            userID = payload['events'][0]['source']['userId']
            userProfile = GetUserProfile(userID,Channel_Access_Token)
            orderTo,task,by = InsertTask(message,userProfile,userID,groupID)
            replyMessage = 'สั่งงานคุณ: {}\nรายละเอียดงาน: {}\nกำหนดส่ง: {}\nสั่งโดย: {}'.format(orderTo,task,by,userProfile)
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'push' in message :
            PushMessage(Channel_Access_Token)
        if 'งาน' in message or 'มีงาน' in message :
            userID = payload['events'][0]['source']['userId']
            profile = GetUserProfile(userID,Channel_Access_Token)
            ReplyTaskMessage(replyToken,FindTask(profile),Channel_Access_Token)

        return request.json,200
        
    elif request.method == 'GET' :
        return 'this is method GET', 200

    else:
        abort(400)

def FindTask(userProfile):
    reply = []
    # results = collection.find({"order_to":userProfile},{"_id":0,"order_to":0,"task":1,"deadline":1,"created_at":1,"order_by":1,"done_at":0})
    results = collection.find({"order_to":userProfile})
    for result in results:
        messageBack = {"type":"text",
                    "text":"งาน : {}\nกำหนดส่ง : {}\nสั่งโดย : {}\nตั้งแต่วันที่ : {}".format(result["task"],result["deadline"],result["order_by"],result["created_at"])
                    }
        reply.append(messageBack)
    return reply

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
                "done_at":"",
                "order_by":userProfile,
                "from_id":userID,
                "group_id":groupID,
                "status":"In Progress"}

        collection.insert_one(data)

    return nameTag,task,by

def ReplyTaskMessage(ReplyToken,ReplyMessage,ChannelAccessToken):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": ReplyToken,
        "messages":ReplyMessage
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

def ReplyMessage(ReplyToken, TextMessage, ChannelAccessToken):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": ReplyToken,
        "messages":[{
            "type":"text",
            "text":"รับทราบค่ะ"
        },{
            "type":"text",
            "text":TextMessage
        }]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

def PushMessage(ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/multicast'
    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "to": ["Ucb533ae43957da0da8ef0289843f6ae6","U4bb6255362dbd86c9b941d36f85cb8d1","Uae4fc581117126f7ac87e1096ed77ead"],
        "messages":[{
            "type":"text",
            "text":"มีข้อความเข้าในกลุ่ม CE-Project 2020 ค่ะ"
        }]
    }
    data = json.dumps(data)

    r = requests.post(api,headers=headers,data=data)
    
    return 200

