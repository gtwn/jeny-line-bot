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

def ReplyRmdMessage(ReplyToken, ChannelAccessToken):
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
            {
                "type": "flex",
                "altText": "Flex Message",
                "contents": {
                    "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/16/bHCVfS.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "20:13"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "คำสั่งในการสั่งงาน",
                            "size": "lg",
                            "color": "#ffb75e",
                            "flex": 0,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#สั่งงาน @name #งาน รายละเอียดงาน...",
                            "size": "sm",
                            "color": "#ffffff"
                        },
                        {
                            "type": "text",
                            "text": "#ส่ง วัน/เดือน",
                            "size": "sm",
                            "color": "#ffffff"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "คำสั่งดูงานที่ต้องทำ",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#งานที่ต้องทำ",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "คำสั่งดูงานที่สั่ง",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#งานที่สั่ง",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff",
                            "weight": "regular"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "ตรวจสอบงานผ่านเว็บไซต์",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "www..",
                            "margin": "md",
                            "size": "sm",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "http://linecorp.com/"
                            },
                            "color": "#ffffff"
                        }
                        ]
                    }
                    ],"backgroundColor": "#454545"
                    }
                }
                
            }
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
        "messages":ReplyMessage
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