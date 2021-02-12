from flask import Flask ,  request, abort
from Project.Line.flex import *

import requests
import json

def ReplyQuickMessageSayJeny(ReplyToken,GroupID,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    if GroupID == '':
        data = {
            "replyToken": ReplyToken,
            "messages":[{
                "type":"text",
                "text":"สามารถเลือกคำสั่งที่ต้องการตามรายการด้านล่าง",
                "quickReply": QuickReply()
            }
            ]
            
        }
    else:
        data = {
            "replyToken": ReplyToken,
            "messages":[{
                "type":"text",
                "text":"สามารถเลือกคำสั่งที่ต้องการตามรายการด้านล่าง",
                "quickReply":{
                    "items":[
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbUsKf.png",
                            "action": {
                                "type":"message",
                                "label":"คำสั่งแนะนำ",
                                "text":"#คำสั่งแนะนำ"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbEczR.png",
                            "action": {
                                "type":"postback",
                                "label":"สั่งงาน",
                                "text": "สั่งงาน",
                                "data": "action=assign&groupId={}".format(GroupID)
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqMGz.png",
                            "action": {
                                "type":"message",
                                "label":"งานที่สั่ง",
                                "text":"#งานที่สั่ง"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqaB1.png",
                            "action": {
                                "type":"message",
                                "label":"งานที่ต้องทำ",
                                "text":"#งานที่ต้องทำ"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb50qR.png",
                            "action": {
                                "type":"message",
                                "label":"ยกเลิกงาน",
                                "text":"#ยกเลิก"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb5pJe.png",
                            "action": {
                                "type":"message",
                                "label":"ประวัติงาน",
                                "text":"#ประวัติงาน"
                            }
                        }
                    ]
                }
            }]
        }
    data = json.dumps(data)

    r = requests.post(api,headers=headers,data=data)

    return 200

def ReplyNewTask(GroupId, FlexMessage,UserIDs, ChannelAccessToken):
    LINE_API_MultiCast = 'https://api.line.me/v2/bot/message/multicast'
    LINE_API_Push = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "to": GroupId,
        "messages":[FlexMessage]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)
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
                "text":"มีการสั่งงานเข้ามาใหม่\nกรุณาตรวจสอบงานด้วยค่ะ",
                "quickReply": QuickReply()
            }
            ]
    }

    mymessage = json.dumps(mymessage)
    resp1 = requests.post(LINE_API_Push,headers=headers,data=data)
    resp2 = requests.post(LINE_API_Reply,headers=headers,data=mymessage)
    
    return 200


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
                "text":"มีการสั่งงานเข้ามาใหม่\nกรุณาตรวจสอบงานด้วยค่ะ",
                "quickReply": QuickReply()
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
            "text":"ไม่สามารถสั่งงานย้อนหลังได้ค่ะ",
            "quickReply": QuickReply()
        }]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)

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
    m = Menu()
    data = {
        "replyToken": ReplyToken,
        "messages":[
            Menu(),
            {
                "type": "image",
                "originalContentUrl": "https://sv1.picz.in.th/images/2021/02/12/oK6QsE.jpg",
                "previewImageUrl": "https://sv1.picz.in.th/images/2021/02/12/oK6QsE.th.jpg"
            }
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
    LINE_API_MultiCast = 'https://api.line.me/v2/bot/message/multicast'
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
                "text":"ติดตามงาน {}\nเรียบร้อย".format(msg['task']),
                "quickReply": QuickReply()
            }
        ]
    }
    #ส่งให้คนถูกสั่งงาน
    bb = BubbleFollow(msg)
    sendToOR = {
        "to": msg["member_id"],
        "messages": [
            bb ]
    }

    msgToME = json.dumps(sendToCMD)
    msgToOR = json.dumps(sendToOR)
    resME = requests.post(api,headers=headers,data=msgToME)
    resOR = requests.post(LINE_API_MultiCast,headers=headers,data=msgToOR)
    
    return 200

# ก่อนส่งงาน
def ReplyInfoTask(replyToken,msg, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
   
    #ส่ง info ให้เรา
    bb = BubbleInfoTask(msg)
    sendToOR = {
        "replyToken": replyToken,
        "messages": [
            bb
        ]
    }

    data = json.dumps(sendToOR)
    resOR = requests.post(api,headers=headers,data=data)
    
    return 200

def ReplyInfoCancelTask(replyToken,msg, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
   
    #ส่ง info ให้เรา
    data = {
        "replyToken": replyToken,
        "messages": [
            msg
        ]
    }

    data = json.dumps(data)
    resOR = requests.post(api,headers=headers,data=data)
    
    return 200

## ส่งเมื่อกด Send Work
def ReplyReviewTask(msg,replyToken,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'
    replyAPI = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }
    #ส่งยืนยันการส่งงาน
    sendToCMD = {
        "replyToken": replyToken,
        "messages":[{
                "type":"text",
                "text":"ส่งงาน {}\nเรียบร้อย\nรอการตรวจสอบ".format(msg['task']),
                "quickReply": QuickReply()
            }
        ]
    }
    #ส่งให้คนตรวจงาน
    bb = BubbleReviewTask(msg)
    sendToOR = {
        "to": msg["from_id"],
        "messages": [
            bb
        ]
    }

    msgToME = json.dumps(sendToCMD)
    msgToOR = json.dumps(sendToOR)

    resME = requests.post(replyAPI,headers=headers,data=msgToME)
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
        "messages": [
            ReplyMessage
        ]
    }
    data = json.dumps(data) ## Dump dict >> Json obj
    # print('data : ',data)

    r = requests.post(LINE_API,headers=headers,data=data)
    
    return 200

## ยืนยันการส่งงาน
def ReplyAcceptRejectMessage(msg,status, ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'
    multiple = 'https://api.line.me/v2/bot/message/multicast'
    setAPI = ''
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
                "text":"ตรวจงาน: {}\nสถานะ: {}".format(msg["task"],status),
                "quickReply": QuickReply()
            }
        ]
    }
    #ส่งยืนยันการตรวจสอบงานให้ผู้ถูกสั่งงาน
    sendToOR = {
        "to": msg["member_id"],
        "messages":[{
                "type":"text",
                "text":"คุณ: {}\nตรวจงาน: {}\nสถานะ: {}".format(msg["order_by"],msg["task"],status),
                "quickReply": QuickReply()
            }
        ]
    }


    msgToOR = json.dumps(sendToOR)
    msgToME = json.dumps(sendToCMD)
    resME = requests.post(api,headers=headers,data=msgToME)
    resOR = requests.post(multiple,headers=headers,data=msgToOR)
    
    return 200


## ไม่สามารถทำรายการได้
def ReplyErrorTransaction(ReplyToken,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }

    sendToCMD = {
        "replyToken": ReplyToken,
        "messages":[{
                "type":"text",
                "text":"ไม่สามารถทำรายการได้",
                "quickReply": QuickReply()
            }
        ]
    }

    data = json.dumps(sendToCMD)
    resME = requests.post(api,headers=headers,data=data)

    return 200

# แจ้งเตือนผู้ถูกสั่งงานเมื่อมีการยกเลิกงาน
def ReplyCancelTask(ReplyToken,ReplyMessage,task,ChannelAccessToken):
    API = 'https://api.line.me/v2/bot/message/push'
    REPLY = 'https://api.line.me/v2/bot/message/reply'
    Multiple = 'https://api.line.me/v2/bot/message/multicast'

    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    responseFlex = {
        "replyToken": ReplyToken,
        "messages": [
            ReplyMessage
        ]
    }

    resU = {
        "to": task["member_id"],
        "messages": [{
            "type": "message",
            "text": "คุณ {}\nทำการยกเลิกงาน\n{}\nของคุณ".format(task["order_by"],task["task"]),
            "quickReply": QuickReply()
        }]
    }
    
    respUser = json.dumps(resU)
    res = json.dumps(responseFlex)
    r = requests.post(Multiple,headers=headers,data=respUser)
    resp = requests.post(REPLY,headers=headers,data=res)

    return 200

def NotifyTask(userID,message,ChannelAccessToken):
    api = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer {}'.format(ChannelAccessToken)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': Authorization
    }

    data = {
        "to": userID,
        "messages":[
            message
            
        ]
    }

    data = json.dumps(data)

    r = requests.post(api,headers=headers,data=data)
    
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




def GetUserIdsFollowBot(ChannelAccessToken):
    api = "https://api.line.me/v2/bot/followers/ids"
    Authorization = 'Bearer {}'.format(ChannelAccessToken)
    headers = {
        'Authorization': Authorization
    }
    res = requests.get(api, headers=headers)
    jsLoads = json.loads(res.text)
    return jsLoads["userIds"]