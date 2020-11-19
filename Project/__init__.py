from flask import Flask ,  request, abort
from Project.Line.lineAPI import *
from Project.Line.flex import *
import requests
import json
from datetime import datetime
from Project.Config import *

from Project.Config import *
from Project.db.FindFunction import *
from Project.db.InsertFunction import *
from Project.db.UpdateFunction import *
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
        
        eventsType = payload['events'][0]['type']

        if eventsType == 'join' or eventsType == 'follow':
            replyMsg = FlexRmd()
            ReplyHelloMessage(replyToken,replyMsg,Channel_Access_Token)
        else:
            message = payload['events'][0]['message']['text']
            sourceType = payload['events'][0]['source']['type']
            userID = payload['events'][0]['source']['userId']

            if sourceType == 'group' :
                groupID = payload['events'][0]['source']['groupId']
            else:
                groupID = ''

            if '#สั่งงาน' in message:     # #สั่งงาน @name #งาน รายละเอียดงาน #ส่ง วัน/เดือน
                profile = GetUserProfile(userID,Channel_Access_Token)
                print('groupid:',groupID)
                memberIds = GetMemberUserIDs(groupID,Channel_Access_Token)
                listIDs = ast.literal_eval(memberIds) ## แปลง string  เป็น list <class dict>
                print(listIDs)
                orderTo,task,deadline = InsertTask(message,profile,userID,groupID,listIDs)
                replyMessage = FlexDetailTask(task,deadline,orderTo,profile)
                # replyMessage = '*รายละเอียดการสั่งงาน*\nสั่งงานคุณ: `@{}`\nรายละเอียดงาน: {}\nกำหนดส่ง: {}\nสั่งโดย: `@{}`'.format(orderTo,task,by,profile)
                ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
            if '#คำสั่งแนะนำ' in message:
                # replyMsg = '*คำสั่งแนะนำ*\n*ต้องการสั่งงาน*:\n`Jeny #Order @... #Task .... #By date/month`\n*ต้องการดูงานที่ต้องทำ*: `#งานที่ต้องทำ`\n*ต้องการดูงานที่สั่ง*: `#งานที่สั่ง`'
                replyMsg = FlexRmd()
                ReplyRmdMessage(replyToken,replyMsg,Channel_Access_Token)
                # PushMessage(Channel_Access_Token)
            if '#งานที่ต้องทำ' in message :
                profile = GetUserProfile(userID,Channel_Access_Token)
                if groupID == '':
                    task = FindTask(userID)
                else:
                    task = FindTaskInGroup(userID,groupID)
                reply = FlexMyTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            if '#งานที่สั่ง' in message :
                profile = GetUserProfile(userID,Channel_Access_Token)
                print('groupID:',groupID)
                if groupID == '':
                    task = FindFollowTask(userID)
                else:
                    task = FindFollowTaskInGroup(userID,groupID)
                # print('return task:',task)
                reply = FlexFollowTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            if '#ยกเลิกงาน' in message:
                profile = GetUserProfile(userID,Channel_Access_Token)
                memberIds = GetMemberUserIDs(groupID,Channel_Access_Token)
                listIDs = ast.literal_eval(memberIds) ## แปลง string  เป็น list <class dict>
                task,user = RejectTask(message,listIDs,userID)
                reply = FlexRejectTask(task,user)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
        # else :
        #     ReplyTaskMessage(replyToken,'คำสั่งแนะนำ\n ต้องการสั่งงาน:\n Jeny #Order @... #Task .... #By date/month\n ต้องการดูงานที่ต้องทำ: #งานที่ต้องทำ\n',Channel_Access_Token)
        return request.json,200
        
    elif request.method == 'GET' :
        return 'this is method GET', 200

    else:
        abort(400)


