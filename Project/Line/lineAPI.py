from flask import Flask ,  request, abort

import requests
import json



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
        },TextMessage]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    print('data : ',data)

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

    data = {
        "replyToken": ReplyToken,
        "messages":[
            msg
        ]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

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
    print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

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