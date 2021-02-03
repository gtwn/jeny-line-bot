from datetime import datetime
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *
from Project.Config import *
from Project.Line.lineAPI import *
from bson.objectid import ObjectId


from Project.Line.lineAPI import *
from Project.Line.flex import *


collection = db["tasks"]
true = True
## งานที่ต้องทำ
def FindTask(userID):
    reply = []
    results = collection.find({"member_id": {"$elemMatch":{"$eq":userID}},"status":"In Progress"}).sort('deadline', pymongo.ASCENDING).limit(5)
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            # status = 'เกินกำหนด'
            color = "#FF4646FF"
        else:
            # status = 'ยังไม่เลยกำหนด'
            color = "#000000FF"
        messageTask = {
            "type": "box",
            "layout": "baseline",
            "action" : {
                "type": "postback",
                "text": "รายละเอียดงาน {}".format(result["task"]),
                "data": "action=information&id={}".format(str(result["_id"]))
            },
            "contents": [
            {
                "type": "text",
                "text": result["task"],
                "contents": []
            },
            {
                "type": "text",
                "text": deadline,
                "color": color,
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageTask)
        messageGroup = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "กลุ่ม:",
                "weight": "bold",
                "contents": []
            },
            {
                "type": "text",
                "text": result["group_name"],
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageGroup)
        space = {
            "type": "separator",
            "margin": "sm",
            "color": "#DDDDDDFF"
        }
        reply.append(space)
    return reply

## งานที่ต้องทำในกลุ่ม
def FindTaskInGroup(userID,groupID):
    reply = []
    results = collection.find({"member_id": {"$elemMatch":{"$eq":userID}},"group_id":groupID,"status":"In Progress"}).sort('deadline', pymongo.ASCENDING).limit(5)
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            # status = 'เกินกำหนด'
            color = "#FF4646FF"
        else:
            # status = 'ยังไม่เลยกำหนด'
            color = "#000000FF"

        messageTask = {
            "type": "box",
            "layout": "baseline",
            "action" : {
                "type": "postback",
                "text": "รายละเอียดงาน {}".format(result["task"]),
                "data": "action=information&id={}".format(str(result["_id"]))
            },
            "contents": [
            {
                "type": "text",
                "text": result["task"],
                "contents": []
            },
            {
                "type": "text",
                "text": deadline,
                "color": color,
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageTask)
        messageGroup = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "กลุ่ม:",
                "weight": "bold",
                "contents": []
            },
            {
                "type": "text",
                "text": result["group_name"],
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageGroup)
        space = {
            "type": "separator",
            "margin": "sm",
            "color": "#DDDDDDFF"
        }
        reply.append(space)

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
            color = "#000000FF"
        messageTask = {
            "type": "box",
            "layout": "baseline",
            "action" : {
                "type": "postback",
                "text": "รายละเอียดงาน {}".format(result["task"]),
                "data": "action=followinfo&id={}".format(str(result["_id"]))
            },
            "contents": [
            {
                "type": "text",
                "text": result["task"],
                "contents": []
            },
            {
                "type": "text",
                "text": deadline,
                "color": color,
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageTask)
        messageUser = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "ผู้รับผิดชอบ:",
                "weight": "bold",
                "contents": []
            },
            {
                "type": "text",
                "text": "{}".format("@"+" @".join(result["member"])),
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageUser)
        space = {
            "type": "separator",
            "margin": "sm",
            "color": "#DDDDDDFF"
        }
        reply.append(space)
        
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
            color = "#000000FF"

        messageTask = {
            "type": "box",
            "layout": "baseline",
            "action" : {
                "type": "postback",
                "text": "รายละเอียดงาน {}".format(result["task"]),
                "data": "action=followinfo&id={}".format(str(result["_id"]))
            },
            "contents": [
            {
                "type": "text",
                "text": result["task"],
                "contents": []
            },
            {
                "type": "text",
                "text": deadline,
                "color": color,
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageTask)
        messageUser = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "ผู้รับผิดชอบ:",
                "weight": "bold",
                "contents": []
            },
            {
                "type": "text",
                "text": "{}".format("@"+" @".join(result["member"])),
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageUser)
        space = {
            "type": "separator",
            "margin": "sm",
            "color": "#DDDDDDFF"
        }
        reply.append(space)

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
            color = "#000000FF"
        
        messageTask = {
            "type": "box",
            "layout": "baseline",
            "action": {
                "type": "postback",
                "label": "ยกเลิกงาน"+result["task"],
                "text":"ตรวจสอบการยกเลิกงาน\n{}\nผู้รับผิดชอบ: {}".format(result["task"],"@"+" @".join(result["member"])),
                "data": "action=removeInfo&id={}".format(str(result["_id"]))
            },
            "contents": [
            {
                "type": "text",
                "text": result["task"],
                "contents": []
            },
            {
                "type": "text",
                "text": deadline,
                "color": color,
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageTask)
        messageUser = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "ผู้รับผิดชอบ:",
                "weight": "bold",
                "contents": []
            },
            {
                "type": "text",
                "text": "{}".format("@"+" @".join(result["member"])),
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageUser)
        space = {
            "type": "separator",
            "margin": "sm",
            "color": "#DDDDDDFF"
        }
        reply.append(space)
        
    return reply


## ยกเลิกงานที่สั่งในกลุ่ม
def RejectFollowTaskInGroup(userID,groupID):
    reply = [] 
    results = collection.find({"from_id":userID,"group_id":groupID, "status":"In Progress"})
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            # status = 'เกินกำหนด'
            color = "#FF4646FF"
        else:
            # status = 'ยังไม่เลยกำหนด'
            color = "#000000FF"
        
        messageTask = {
            "type": "box",
            "layout": "baseline",
            "action": {
                "type": "postback",
                "label": "ยกเลิกงาน"+result["task"],
                "text":"ตรวจสอบการยกเลิกงาน\n{}\nผู้รับผิดชอบ: {}".format(result["task"],"@"+" @".join(result["member"])),
                "data": "action=removeInfo&id={}".format(str(result["_id"]))
            },
            "contents": [
            {
                "type": "text",
                "text": result["task"],
                "contents": []
            },
            {
                "type": "text",
                "text": deadline,
                "color": color,
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageTask)
        messageUser = {
            "type": "box",
            "layout": "baseline",
            "contents": [
            {
                "type": "text",
                "text": "ผู้รับผิดชอบ:",
                "weight": "bold",
                "contents": []
            },
            {
                "type": "text",
                "text": "{}".format("@"+" @".join(result["member"])),
                "align": "end",
                "contents": []
            }
            ]
        }
        reply.append(messageUser)
        space = {
            "type": "separator",
            "margin": "sm",
            "color": "#DDDDDDFF"
        }
        reply.append(space)

    return reply

def FindHistory(userID,groupID):
    reply = [] 

    # รายบุคคล
    if groupID == '':
        results = collection.find({"$and":[{"$or":[{"status":"Reject"},{"status":"Done"}]},{"$or":[{"member_id": {"$elemMatch":{"$eq":userID}}},{"from_id":userID}]}]}).sort('done_at',pymongo.DESCENDING).limit(5)
    else:
        results = collection.find({"$and":[{"$or":[{"status":"Reject"},{"status":"Done"}]},{"$or":[{"member_id": {"$elemMatch":{"$eq":userID}}},{"from_id":userID}]},{"group_id":groupID}]}).sort('done_at',pymongo.DESCENDING).limit(5)   #ในกลุ่ม

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
                        "text": "{}".format('@'+" @".join(result["member"])),
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
            color = "#000000FF"
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
                                    "type": "postback",
                                    "label": "ตามงาน"+result["task"],
                                    "text": "ติดตามงาน\n{}".format(result["task"]),
                                    "data": "action=follow&id={}".format(str(result["_id"]))
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
                        "text": "{}".format("@"+" @".join(result["member"])),
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
                "text": result["group_name"],
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

## ตรวจสอบงานรอรีวิว
def FindReviewTask(userID):
    reply = [] 
    results = collection.find({"from_id":userID, "status":"Review"})
    for result in results:
       
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
            color = "#FF4646FF"

        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#000000FF"
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
                                    "type": "postback",
                                    "text": "ตรวจงาน\n{}".format(result["task"]),
                                    "data": "action=ifcheck&id={}".format(str(result["_id"]))
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
                        "text": "{}".format("@"+" @".join(result["member"])),
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
                "text": result["group_name"],
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


#ส่งงาน
def ListTaskForSend(userID):
    reply = [] 
    results = collection.find({"member_id": {"$elemMatch":{"$eq":userID}}, "status":"In Progress"})
    for result in results:
        deadline = datetime.strftime(result["deadline"],"%d %b, %Y")
        createAt = datetime.strftime(result["created_at"],"%d %b, %Y")
        if datetime.now() > result['deadline'] :
            status = 'เกินกำหนด'
            color = "#FF4646FF"

        else:
            status = 'ยังไม่เลยกำหนด'
            color = "#000000FF"

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
                                    "type": "postback",
                                    "text": "ตรวจสอบข้อมูลการส่งงาน\n{}".format(result["task"]),
                                    "data": "action=info&id={}".format(str(result["_id"]))
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
                "text": result["group_name"],
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


def FindTaskNotiToday(userIds):

    task = []
    now = datetime.now()
    dateString = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
    dateObj = datetime.strptime(dateString, '%Y-%m-%d')

    for Id in userIds:
        task = []
        results = collection.find({"member_id": {"$elemMatch":{"$eq":Id}},"status":"In Progress","deadline":dateObj})
        for result in results:
            print("r",result)
            tFlex = {
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
                            "action": {
                                "type": "postback",
                                "text": "ตรวจสอบข้อมูลการส่งงาน\n{}".format(result["task"]),
                                "data": "action=info&id={}".format(str(result["_id"]))
                            },
                            "contents": []
                        }
                        ]
            }
            task.append(tFlex)
            orderFlex = {
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
                            "text": result["order_by"],
                            "weight": "bold",
                            "color": "#5AD5C1FF",
                            "align": "end",
                            "contents": []
                        }
                        ]
            }
            task.append(orderFlex)
            sp = {
                        "type": "separator",
                        "margin": "lg",
                        "color": "#ECB865"
                    }

            task.append(sp)

        message = FlexTaskToday(task)
        NotifyTask(Id,message,Channel_Access_Token)

    return "Success"