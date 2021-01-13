from flask import Flask ,  request, abort
from Project.Line.flex import *

import requests
import json


# reply คำสั่งงาน
def ReplyMessage(ReplyToken, TextMessage, ChannelAccessToken,UserIDs):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    LINE_API_MultiCast = 'https://api.line.me/v2/bot/message/multicast'
    LINE_API_Push = 'https://api.line.me/v2/bot/message/push'
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
        },TextMessage]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)
    print('UserIDs',UserIDs)
    if len(UserIDs) == 1 :
        LINE_API_Reply = LINE_API_Push
        ID = UserIDs[0]
        
    else:
        LINE_API_Reply = LINE_API_MultiCast
        ID = UserIDs
  
    mymessage = {
            "to": ID,
            "messages": [ {
                "type":"text",
                "text":"มีการสั่งงานเข้ามาใหม่\nกรุณาตรวจสอบงานด้วยค่ะ"
            }
            ]
    }

    print('Line',LINE_API_Reply)
    print('ID',ID)
    mymessage = json.dumps(mymessage)
    r = requests.post(LINE_API,headers=headers,data=data)
    rp = requests.post(LINE_API_Reply,headers=headers,data=mymessage)
    
    print(rp)
    return 200

def ReplyRejectMessage(ReplyToken, ChannelAccessToken):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": ReplyToken,
        "messages": [{"type":"text",
            "text":"ไม่สามารถสั่งงานย้อนหลังได้ค่ะ"}]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

def ReplyRmdMessage(ReplyToken,msg, ChannelAccessToken):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    # headers = {
    #     'Content-Type': 'application/json; charset=UTF-8',
    #     'Authorization': Authorization
    # }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
    m = Menu()
    data = {
        "replyToken": ReplyToken,
        "messages":[
            Menu()
        ]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

## แสดงตอน Add BOT
def ReplyHelloMessage(ReplyToken,msg, ChannelAccessToken):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    # headers = {
    #     'Content-Type': 'application/json; charset=UTF-8',
    #     'Authorization': Authorization
    # }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }

    data = {
        "replyToken": ReplyToken,
        "messages":[{
            "type":"text",
            "text":"สวัสดีค่าต้องการให้ Jeny ช่วยบันทึกงาน\nดูคำสั่งแนะนำการใช้งานตามด่านล่าง\nรบกวนทุกคนแอด Jeny เป็นเพื่อนก่อนใช้งานด้วยนะคะ"
        },
            msg
        ]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

## ตามงาน
def ReplyFollowTask(msg, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
    #ส่งยืนยันการตามงาน
    sendToCMD = {
        "to": msg["from_id"],
        "messages":[{
                "type":"text",
                "text":"ติดตามงานเรียบร้อย"
            }
        ]
    }
    #ส่งให้คนถูกสั่งงาน
    bb = BubbleFollow(msg)
    print("bb:",bb)
    sendToOR = {
        "to": msg["from_id"],
        "messages": [bb]
    }

    msgToME = json.dumps(sendToCMD)
    msgToOR = json.dumps(sendToOR)
    resME = requests.post(api,headers=headers,data=msgToME)
    resOR = requests.post(api,headers=headers,data=msgToOR)
    
    return 200

# ก่อนส่งงาน
def ReplyInfoTask(userID,msg, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
   
    #ส่ง info ให้เรา
    bb = BubbleInfoTask(msg)
    sendToOR = {
        "to": userID,
        "messages": [bb]
    }

    data = json.dumps(sendToOR)
    resOR = requests.post(api,headers=headers,data=data)
    
    return 200

## ส่งเมื่อกด Send Work
def ReplyReviewTask(msg, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
    #ส่งยืนยันการตามงาน
    sendToCMD = {
        "to": msg["from_id"],
        "messages":[{
                "type":"text",
                "text":"ส่งงานเรียบร้อย รอการตรวจสอบ"
            }
        ]
    }
    #ส่งให้คนตรวจงาน
    bb = BubbleReviewTask(msg)
    sendToOR = {
        "to": msg["from_id"],
        "messages": [bb]
    }

    msgToME = json.dumps(sendToCMD)
    msgToOR = json.dumps(sendToOR)
    resME = requests.post(api,headers=headers,data=msgToME)
    resOR = requests.post(api,headers=headers,data=msgToOR)
    
    return 200

# ตอบกลับคำสั่งขอดูงาน
def ReplyTaskMessage(ReplyToken,ReplyMessage,ChannelAccessToken):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": ReplyToken,
        "messages": [ReplyMessage]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

## ยืนยันการส่งงาน
def ReplyAcceptRejectMessage(msg,status, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
    #ส่งยืนยันการยอมรับงาน
    sendToCMD = {
        "to": msg["from_id"],
        "messages":[{
                "type":"text",
                "text":"ตรวจงาน:"+msg["task"]+"\nสถานะ: "+status
            }
        ]
    }
    #ส่งยืนยันการตรวจสอบงานให้ผู้ถูกสั่งงาน
    sendToOR = {
        "to": msg["from_id"],
        "messages":[{
                "type":"text",
                "text":"คุณ:"+msg["order_by"]+"\nตรวจงาน: "+msg["task"]+"\nสถานะ: "+status
            }
        ]
    }

    msgToME = json.dumps(sendToCMD)
    msgToOR = json.dumps(sendToOR)
    resME = requests.post(api,headers=headers,data=msgToME)
    resOR = requests.post(api,headers=headers,data=msgToOR)
    
    return 200


## ไม่สามารถทำรายการได้
def ReplyErrorTransaction(userID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
    #ส่งยืนยันการยอมรับงาน
    sendToCMD = {
        "to": userID,
        "messages":[{
                "type":"text",
                "text":"ไม่สามารถทำรายการได้"
            }
        ]
    }

    data = json.dumps(sendToCMD)
    resME = requests.post(api,headers=headers,data=data)

    return 200




def GetGroupSummary(GroupID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/group/{}/summary'.format(GroupID)
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    resp = requests.get(api,headers=headers)
    jsLoads = json.loads(resp.text)
    return jsLoads["groupName"]

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


def PushMessage(ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push '
    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }

    data = {
        "to": "Uae4fc581117126f7ac87e1096ed77ead",
        "messages":[
            {"type": "flex",
            "altText": "This is a Flex Message",
            "contents": {
                "type": "bubble",
                "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                    "type": "text",
                    "text": "Hello,"
                    },
                    {
                    "type": "text",
                    "text": "World!"
                    }
                ]
                }
            }
            }
        ]
    }
    data = json.dumps(data)

    r = requests.post(api,headers=headers,data=data)
    
    return 200