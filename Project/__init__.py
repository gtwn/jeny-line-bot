from flask import Flask ,  request, abort
from Project.Line.lineAPI import *
import requests
import json
from datetime import datetime
from Project.Config import *

from Project.Config import *
from Project.db.FindFunction import *
from Project.db.InsertFunction import *
import ast

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
        eventsType = payload['events'][0]['type']
        if sourceType == 'group' :
            groupID = payload['events'][0]['source']['groupId']
        else:
            groupID = ' '
        if 'Hi' in message :
            
            replyMessage = 'Say Hi from ' + userID + 'in groupID' + groupID
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'jeny' in message.lower() and '#order' in message.lower():
            profile = GetUserProfile(userID,Channel_Access_Token)
            memberIds = GetMemberUserIDs(groupID,Channel_Access_Token)
            listIDs = ast.literal_eval(memberIds) ## แปลง string  เป็น list <class dict>
            orderTo,task,by = InsertTask(message,profile,userID,groupID,listIDs)
            replyMessage = 'สั่งงานคุณ: `@{}`\nรายละเอียดงาน: {}\nกำหนดส่ง: {}\nสั่งโดย: `@{}`'.format(orderTo,task,by,profile)
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        if 'jeny' in message and 'คำแนะนำ' in message:
            replyMsg = 'คำสั่งแนะนำ\n ต้องการสั่งงาน:\n Jeny #Order @... #Task .... #By date/month\n ต้องการดูงานที่ต้องทำ: #งานที่ต้องทำ\n ต้องการดูงานที่สั่ง: #งานที่สั่ง'
            ReplyMessage(replyToken,replyMsg,Channel_Access_Token)
        if 'jeny' in message.lower() and '#งานที่ต้องส่ง' in message or '#งานที่ต้องทำ' in message :
            profile = GetUserProfile(userID,Channel_Access_Token)
            ReplyTaskMessage(replyToken,userID,Channel_Access_Token)
        if 'jeny' in message.lower() and '#งานที่สั่ง' in message :
            profile = GetUserProfile(userID,Channel_Access_Token)
            ReplyTaskMessage(replyToken,userID,Channel_Access_Token)
        else :
            ReplyTaskMessage(replyToken,'คำสั่งแนะนำ\n ต้องการสั่งงาน:\n Jeny #Order @... #Task .... #By date/month\n ต้องการดูงานที่ต้องทำ: #งานที่ต้องทำ\n',Channel_Access_Token)
        return request.json,200
        
    elif request.method == 'GET' :
        return 'this is method GET', 200

    else:
        abort(400)


