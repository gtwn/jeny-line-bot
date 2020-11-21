from datetime import datetime
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *

collection = db["task"]
true = True
## งานที่ต้องทำ
def FindTask(userID):
    reply = []
    # results = collection.find({"order_to":userProfile},{"_id":0,"order_to":0,"task":1,"deadline":1,"created_at":1,"order_by":1,"done_at":0})
    results = collection.find({"order_id":userID,"status":"In Progress"}).sort('deadline', pymongo.ASCENDING)
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
            color = "#FF4646FF"
        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#FFFFFFFF"

        messageBack = {
                        "type": "box",
                        "layout": "baseline",
                        "paddingBottom": "5px",
                        "contents": [
                        {
                            "type": "text",
                            "text": result["task"],
                            "weight": "bold",
                            "size": "md",
                            "color": "#FFFFFFFF",
                            "align": "start",
                            "wrap": true,
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": deadline,
                            "weight": "bold",
                            "size": "md",
                            "color": color,
                            "align": "end",
                            "contents": []
                        }
                        ]
        }
        reply.append(messageBack)

    return reply

## งานที่ต้องทำในกลุ่ม
def FindTaskInGroup(userID,groupID):
    reply = []
    # results = collection.find({"order_to":userProfile},{"_id":0,"order_to":0,"task":1,"deadline":1,"created_at":1,"order_by":1,"done_at":0})
    results = collection.find({"order_id":userID,"group_id":groupID,"status":"In Progress"})
    for result in results:
        print('result:',result)
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
            color = "#FF4646FF"
        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#FFFFFFFF"

        messageBack = {
                        "type": "box",
                        "layout": "baseline",
                        "paddingBottom": "5px",
                        "contents": [
                        {
                            "type": "text",
                            "text": result["task"],
                            "weight": "bold",
                            "size": "md",
                            "color": "#FFFFFFFF",
                            "align": "start",
                            "wrap": true,
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": deadline,
                            "weight": "bold",
                            "size": "md",
                            "color": color,
                            "align": "end",
                            "contents": []
                        }
                        ]
        }
        reply.append(messageBack)

    print('reply:',reply)
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
            color = "#FF4646FF"

        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#FFFFFFFF"
        messageBack = {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "paddingBottom": "5px",
                            "contents": [
                            {
                                "type": "text",
                                "text": result["task"],
                                "weight": "bold",
                                "size": "md",
                                "color": "#FFFFFFFF",
                                "align": "start",
                                "wrap": true,
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": deadline,
                                "weight": "bold",
                                "size": "md",
                                "color": color,
                                "align": "end",
                                "contents": []
                            }
                            ]
                        }
        reply.append(messageBack)
        cmd =   {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ผู้รับผิดชอบ :",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFFFFFFF",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '@'+result["order_to"],
                        "weight": "bold",
                        "color": "#5AD5C1FF",
                        "align": "end",
                        "contents": []
                    }
                    ]
                }
        reply.append(cmd)
        sp  =   {
                "type": "separator",
                "margin": "lg",
                "color": "#ECB865"
                } 
        
        reply.append(sp)
    return reply


## งานที่สั่งในกลุ่ม
def FindFollowTaskInGroup(userID,groupID):
    reply = [] 
    results = collection.find({"from_id":userID,"group_id":groupID, "status":"In Progress"})
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
            color = "#FF4646FF"

        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#FFFFFFFF"

        messageBack = {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "paddingBottom": "5px",
                            "contents": [
                            {
                                "type": "text",
                                "text": result["task"],
                                "weight": "bold",
                                "size": "md",
                                "color": "#FFFFFFFF",
                                "align": "start",
                                "wrap": true,
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": deadline,
                                "weight": "bold",
                                "size": "md",
                                "color": color,
                                "align": "end",
                                "contents": []
                            }
                            ]
                        }
        reply.append(messageBack)
        cmd =   {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ผู้รับผิดชอบ :",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFFFFFFF",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '@'+result["order_to"],
                        "weight": "bold",
                        "color": "#5AD5C1FF",
                        "align": "end",
                        "contents": []
                    }
                    ]
                }
        reply.append(cmd)
        sp  =   {
                "type": "separator",
                "margin": "lg",
                "color": "#ECB865"
                } 
        
        reply.append(sp)

    return reply