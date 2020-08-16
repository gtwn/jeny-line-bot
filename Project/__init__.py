from flask import Flask ,  request, abort
import requests
import json
from Project.Config import *

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
    return resp.text

def GetGroupUserProfile(userID,GroupID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/group/{}/member/{}'.format(GroupID,userID)
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    resp = requests.get(api,headers=headers)
    jsLoads = json.loads(resp.text)
    return jsLoads['displayName']

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
            orderTo,task,by = SubString(message)
            replyMessage = 'สั่งงานคุณ: {}\nรายละเอียดงาน: {}\nกำหนดส่ง: {}\nสั่งโดย: {}'.format(orderTo,task,by,GetGroupUserProfile(userID,groupID,Channel_Access_Token))
            ReplyMessage(replyToken,replyMessage,Channel_Access_Token)
        return request.json,200
    elif request.method == 'GET' :
        return 'this is method GET', 200

    else:
        abort(400)



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
            "text":TextMessage
        }]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200


def SubString(message):
    nameTag = ''
    for i in range (message.count('@')) :
        tag = message.split('@')[i+1].split(' ')[0]
        nameTag += tag + ' '
    task = message.split(" ")[3]
    if '#by' not in message.lower() :
        by = 'To night'
    else :
        by = message.lower().split("#by ")[1]

    return nameTag,task,by