from flask import Flask ,  request, abort
from flask_cors import CORS
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
CORS(app)

@app.route('/')
def hello():
    message = json.dumps({"message": "hello"})
    return message, 200

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
        elif eventsType == 'postback':  ## ส่ง action การทำรายการ
            data = payload['events'][0]['postback']['data']
            userID = payload['events'][0]["source"]["userId"]
            r = requests.post('https://099b8ad14268.ngrok.io/action?{}&replyToken={}&userID={}'.format(data,replyToken,userID))
        elif eventsType == 'message':
            message = ((payload['events'][0]['message']['text']).replace('\u200b','')).strip()
            sourceType = payload['events'][0]['source']['type']
            userID = payload['events'][0]['source']['userId']

            if sourceType == 'group' :
                groupID = payload['events'][0]['source']['groupId']
            else:
                groupID = ''
            if message == 'Jeny':
                ReplyQuickMessageSayJeny(replyToken,groupID,Channel_Access_Token) 
            elif '#สั่งงาน' in message:     # #สั่งงาน @name #งาน รายละเอียดงาน #ส่ง วัน/เดือน
                profile = GetUserProfile(userID,Channel_Access_Token)
                print('groupid:',groupID)
                memberIds = GetMemberUserIDs(groupID,Channel_Access_Token)
                listIDs = ast.literal_eval(memberIds) ## แปลง string  เป็น list <class dict>
                print(listIDs)
                orderTo,task,deadline,orderIds = InsertTask(message,profile,userID,groupID,listIDs)
                if not orderTo:
                    ReplyRejectMessage(replyToken,Channel_Access_Token)
                else:
                    replyMessage = FlexDetailTask(task,deadline,orderTo,profile)
                    # replyMessage = '*รายละเอียดการสั่งงาน*\nสั่งงานคุณ: `@{}`\nรายละเอียดงาน: {}\nกำหนดส่ง: {}\nสั่งโดย: `@{}`'.format(orderTo,task,by,profile)
                    ReplyMessage(replyToken,replyMessage,Channel_Access_Token,orderIds)
            elif '#คำสั่งแนะนำ' in message:
                # replyMsg = '*คำสั่งแนะนำ*\n*ต้องการสั่งงาน*:\n`Jeny #Order @... #Task .... #By date/month`\n*ต้องการดูงานที่ต้องทำ*: `#งานที่ต้องทำ`\n*ต้องการดูงานที่สั่ง*: `#งานที่สั่ง`'
                replyMsg = FlexRmd()
                ReplyRmdMessage(replyToken,replyMsg,Channel_Access_Token)
                # PushMessage(Channel_Access_Token)
            elif '#งานที่ต้องทำ' in message :
                profile = GetUserProfile(userID,Channel_Access_Token)
                if groupID == '':
                    task = FindTask(userID)
                else:
                    task = FindTaskInGroup(userID,groupID)
                reply = FlexMyTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#งานที่สั่ง' in message :
                profile = GetUserProfile(userID,Channel_Access_Token)
                if groupID == '':
                    task = FindFollowTask(userID)
                else:
                    task = FindFollowTaskInGroup(userID,groupID)
                # print('return task:',task)
                reply = FlexFollowTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#ยกเลิก' in message:
                profile = GetUserProfile(userID,Channel_Access_Token)
                if groupID == '':
                    task = RejectFollowTask(userID)
                else:
                    task = RejectFollowTaskInGroup(userID,groupID)
                reply = FlexFollowTaskReject(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#ประวัติงาน' in message:
                profile = GetUserProfile(userID,Channel_Access_Token)

                task = FindHistory(userID,groupID)
                reply = HistoryTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#ตามงาน' in message:
                if groupID == '':
                    task = FollowTask(userID)
                    reply = FlexFollow(task)
                    ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#ส่งงาน' in message:
                if groupID == '':
                    task = ListTaskForSend(userID)
                    reply = FlexTaskList(task)
                    ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            # else:
            #     if groupID == '':
            #         replyMsg = FlexRmd()
            #         ReplyHelloMessage(replyToken,replyMsg,Channel_Access_Token)
            #     elif ('#ยก' or '#งาน' or '#สั่ง') in message:
            #         replyMsg = FlexRmd()
            #         ReplyRmdMessage(replyToken,replyMsg,Channel_Access_Token)


        # else :
        #     ReplyTaskMessage(replyToken,'คำสั่งแนะนำ\n ต้องการสั่งงาน:\n Jeny #Order @... #Task .... #By date/month\n ต้องการดูงานที่ต้องทำ: #งานที่ต้องทำ\n',Channel_Access_Token)
        return request.json,200
        
    elif request.method == 'GET' :
        return 'this is method GET', 200

    else:
        abort(400)



@app.route('/notify/task', methods=['GET'])
def notifyTask():
    userIds = GetUserIdsFollowBot(Channel_Access_Token)
    message = FindTaskNotiToday(userIds)
    return message,200


@app.route('/action', methods=['POST'])
def action():
    print('query:',request.query_string)
    action = request.args.get('action')
    id = request.args.get('id')
    userID = request.args.get('userID')
    replyToken = request.args.get('replyToken')
    
    if action == 'follow':      
        result = FindTaskByID(id)
        if result["status"] != 'In Progress':
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            ReplyFollowTask(result,Channel_Access_Token)
    elif action == 'info':
        result = FindTaskByID(id)
        if result["status"] != 'In Progress':
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            ReplyInfoTask(replyToken,result,Channel_Access_Token)
    elif action == 'send':
        result = FindTaskByID(id)
        if result["status"] != 'In Progress':
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            result = ReviewTaskByID(id)
            ReplyReviewTask(result,replyToken,Channel_Access_Token)
    elif action == 'accept':
        result = FindTaskByID(id)
        if result["status"] != 'Review' or result["from_id"] != userID:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            status = 'ผ่านการตรวจสอบ'
            result = AcceptTaskByID(id)
            ReplyAcceptRejectMessage(result,status,Channel_Access_Token)
    elif action == 'reject':
        result = FindTaskByID(id)
        if result["status"] != 'Review' or result["from_id"] != userID:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            status = 'ผ่านการตรวจสอบ'
            result = RejectTaskByID(id)
            ReplyAcceptRejectMessage(result,status,Channel_Access_Token)
    elif action == 'removeInfo':
        result = FindTaskByID(id)
        if result["status"] != 'In Progress' or result["from_id"] != userID:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            message = BubbleInfoBeforeCancel(result)
            ReplyInfoCancelTask(replyToken,message,Channel_Access_Token)
    elif action == 'remove':
        # profile = GetUserProfile(userID,Channel_Access_Token)
        # memberIds = GetMemberUserIDs(groupID,Channel_Access_Token)
        # listIDs = ast.literal_eval(memberIds) ## แปลง string  เป็น list <class dict>
        result = FindTaskByID(id)
        if result["status"] != "In Progress" or result["from_id"] != userID:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            user = RejectTask(id)
            reply = FlexRejectTask(result,user)
            ReplyCancelTask(replyToken,reply,result,Channel_Access_Token)
        
    else :
        ReplyErrorTransaction(replyToken,Channel_Access_Token)

    return request.query_string,200



@app.route('/assign/task', methods=['POST'])
def assignTask():
    groupId = request.headers.get('groupId')
    userOrder = request.headers.get('userId')
    payload = request.json
    print(payload)
    subject = payload.get('subject')
    userList = payload.get('order_to')
    deadline = payload.get('deadline')
    deadline_obj = datetime.strptime(deadline,"%Y-%m-%dT%H:%M:%S.%fZ")
    typeWork = payload.get('type')
    detail = payload.get('detail')
    # print(type(deadline))
    # print(str(date_time_obj.day), str(date_time_obj.month), str(date_time_obj.year))
    if subject == "" and userList == [] and detail == "" and typeWork == "" and deadline == "" :
        return 'Failed', 304
    else :
        flexOrder = InsertNewTask(userList, subject, detail, typeWork, deadline_obj, userOrder, groupId)
        print(flexOrder)
  
    return 'Success',201