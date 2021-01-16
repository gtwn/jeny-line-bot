from datetime import datetime
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *
from Project.Config import *
from Project.Line.lineAPI import *
from bson.objectid import ObjectId


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



## ค้นหางานที่สั่งสำหรับยกเลิก
def RejectFollowTask(userID):
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
                                "action": {
                                    "type": "message",
                                    "label": "ยกเลิกงาน"+result["task"],
                                    "text": "#ยกเลิกงาน "+result["task"]+" @"+result["order_to"]
                                },
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


## ยกเลิกงานที่สั่งในกลุ่ม
def RejectFollowTaskInGroup(userID,groupID):
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
                                "action": {
                                    "type": "message",
                                    "label": "ยกเลิกงาน"+result["task"],
                                    "text": "#ยกเลิกงาน "+result["task"]+" @"+result["order_to"]
                                },
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

def FindHistory(userID,groupID):
    reply = [] 

    # รายบุคคล
    if groupID == '':
        results = collection.find({"$and":[{"$or":[{"status":"Reject"},{"status":"Done"}]},{"$or":[{"order_id":userID},{"from_id":userID}]}]}).sort('done_at',pymongo.DESCENDING).limit(5)
    else:
        results = collection.find({"$and":[{"$or":[{"status":"Reject"},{"status":"Done"}]},{"$or":[{"order_id":userID},{"from_id":userID}]},{"group_id":groupID}]}).sort('done_at',pymongo.DESCENDING).limit(5)   #ในกลุ่ม

    for result in results:
        
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
                                "text": result["status"],
                                "weight": "bold",
                                "size": "md",
                                "color": "#FFFFFFFF",
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
                        "color": "#FF8050FF",
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


## ตามงาน
def FollowTask(userID):
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

        group = GetGroupSummary(result["group_id"],Channel_Access_Token)
        print("group_id:",group)
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
                                "action": {
                                    "type": "message",
                                    "label": "ตามงาน"+result["task"],
                                    "text": "#Follow "+str(result["_id"])+" "+result["task"]
                                },
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
        grp = {
            "type": "box",
            "layout": "baseline",
            "spacing": "xs",
            "margin": "sm",
            "contents": [
              {
                "type": "text",
                "text": "กลุ่ม :",
                "weight": "bold",
                "size": "md",
                "color": "#FFFFFFFF",
                "contents": []
              },
              {
                "type": "text",
                "text": group,
                "weight": "bold",
                "color": "#FFFFFFFF",
                "align": "end",
                "wrap": true,
                "position": "relative",
                "contents": []
              }
            ]
          }
        reply.append(grp)
        sp  =   {
                "type": "separator",
                "margin": "lg",
                "color": "#ECB865"
                } 
        
        reply.append(sp)
    return reply

def ListTaskForSend(userID):
    reply = [] 
    results = collection.find({"order_id":userID, "status":"In Progress"})
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
            color = "#FF4646FF"

        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#FFFFFFFF"

        group = GetGroupSummary(result["group_id"],Channel_Access_Token)
        print("group_id:",group)
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
                                "action": {
                                    "type": "message",
                                    "label": "ตามงาน"+result["task"],
                                    "text": "#Info "+str(result["_id"])+" "+result["task"]
                                },
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
                        "text": "ผู้สั่งงาน :",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFFFFFFF",
                        "align": "start",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": '@'+result["order_by"],
                        "weight": "bold",
                        "color": "#5AD5C1FF",
                        "align": "end",
                        "contents": []
                    }
                    ]
                }
        reply.append(cmd)
        grp = {
            "type": "box",
            "layout": "baseline",
            "spacing": "xs",
            "margin": "sm",
            "contents": [
              {
                "type": "text",
                "text": "กลุ่ม :",
                "weight": "bold",
                "size": "md",
                "color": "#FFFFFFFF",
                "contents": []
              },
              {
                "type": "text",
                "text": group,
                "weight": "bold",
                "color": "#FFFFFFFF",
                "align": "end",
                "wrap": true,
                "position": "relative",
                "contents": []
              }
            ]
          }
        reply.append(grp)
        sp  =   {
                "type": "separator",
                "margin": "lg",
                "color": "#ECB865"
                } 
        
        reply.append(sp)
    return reply

## หางาน by id
def FindTaskByID(taskID):
    result = collection.find_one({"_id": ObjectId(taskID)})
    return result