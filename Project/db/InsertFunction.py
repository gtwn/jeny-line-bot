from datetime import datetime,date
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *
from Project.Line.lineAPI import *


collection = db["task"]

## เพิ่มงาน
def InsertTask(message,userProfile,userID,groupID,memberIds):
    order = []
    userIds = []
    count = 0
    tagCount = message.count('@')
    now = datetime.now()
    # task = message.split("#งาน")[1].split("#")[0]
    listMessage = (message.split('@')[tagCount].split('#ส่ง')[0]).split(' ')
    task = ' '.join(str(x) for x in listMessage[1:])
    by = message.split("#ส่ง")[1].split()[0] + '/'+str(now.year)
    ts =  int(datetime.strptime(by,"%d/%m/%Y").timestamp())
    dt = (datetime.fromtimestamp(int(ts))).strftime('%Y-%m-%d %H:%M:%S')
    dtObj =  datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    if date.today() > dtObj.date():
        print("can't assign")
        # mymessage = {"type":"text",
        #     "text":"ไม่สามารถสั่งงานย้อนหลังได้ค่ะ"}
        # ReplyRejectMessage(replyToken,mymessage,ChannelAccessToken)
        return order,task,by,userIds
    else:
        for uid in memberIds['memberIds']:
            display = GetUserProfile(uid,Channel_Access_Token)
            print(display)
            
            if display in message:

                data = {"order_to":display,
                        "task":task.strip(),
                        "deadline":dtObj,
                        "created_at":datetime.now(),
                        "done_at":datetime.min,
                        "order_by":userProfile,
                        "from_id":userID,
                        "order_id":uid,
                        "group_id":groupID,
                        "status":"In Progress"}

                collection.insert_one(data)
                name = {
                        "type": "text",
                        "text": '@'+display,
                        "weight": "bold",
                        "size": "md",
                        "color": "#F93636FF",
                        "align": "start",
                        "margin": "sm",
                        "wrap": True,
                        "contents": []
                }
                order.append(name)
                userIds.append(uid)
                count += 1
            if count == tagCount:
                break

    return order,task,by,userIds
