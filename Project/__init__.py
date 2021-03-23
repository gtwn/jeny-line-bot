from flask import Flask ,  request, abort
from flask_cors import CORS
from Project.Line.lineAPI import *
from Project.Line.flex import *
import requests
import json
from datetime import datetime
from datetime import timedelta 
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
            ReplyRmdMessage(replyToken,Channel_Access_Token)
        elif eventsType == 'postback':  ## ส่ง action การทำรายการ
            data = payload['events'][0]['postback']['data']
            userID = payload['events'][0]["source"]["userId"]
            r = requests.post('https://jeny-bot.herokuapp.com/action?{}&replyToken={}&userID={}'.format(data,replyToken,userID))
        elif eventsType == 'message':
            message = ((payload['events'][0]['message']['text']).replace('\u200b','')).strip()
            sourceType = payload['events'][0]['source']['type']
            userID = payload['events'][0]['source']['userId']

            if sourceType == 'group' :
                groupID = payload['events'][0]['source']['groupId']
            else:
                groupID = ''
            if message.lower() == 'jeny':
                ReplyQuickMessageSayJeny(replyToken,groupID,Channel_Access_Token) 
            elif '#คำสั่งแนะนำ' in message:
                ReplyRmdMessage(replyToken,Channel_Access_Token)
            elif '#งานที่ต้องทำ' in message :
                if groupID == '':
                    task = FindTask(userID)
                else:
                    task = FindTaskInGroup(userID,groupID)
                reply = FlexMyTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#งานที่สั่ง' in message :
                if groupID == '':
                    task = FindFollowTask(userID)
                else:
                    task = FindFollowTaskInGroup(userID,groupID)
                # print('return task:',task)
                reply = FlexFollowTask(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#ยกเลิก' in message:
                if groupID == '':
                    task = RejectFollowTask(userID)
                else:
                    task = RejectFollowTaskInGroup(userID,groupID)
                reply = FlexFollowTaskReject(task)
                ReplyTaskMessage(replyToken,reply,Channel_Access_Token)
            elif '#ประวัติงาน' in message:
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
    groupID = request.args.get('groupId')
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
    elif action == 'send':      ## ส่ง review งาน
        result = FindTaskByID(id)
        if result["status"] != 'In Progress' or userID not in result["member_id"]:
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
        result = FindTaskByID(id)
        if result["status"] != "In Progress" or result["from_id"] != userID:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            user = RejectTask(id)
            reply = FlexRejectTask(result,user)
            ReplyCancelTask(replyToken,reply,result,Channel_Access_Token)
    elif action == "assign":        ## แสดง flex สำหรับสั่งงาน
        profile = GetUserProfile(userID, Channel_Access_Token)
        replyMessage = FlexAssignTask(profile,groupID)
        ReplyTaskMessage(replyToken, replyMessage, Channel_Access_Token)
    elif action == "information":       ## รายละเอียดงานที่ต้องทำ
        result = FindTaskByID(id)
        if userID not in result["member_id"]:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            reply = FlexInformation(result)
            ReplyTaskMessage(replyToken, reply, Channel_Access_Token)
    elif action == "followinfo":        ## รายละเอียดงานที่สั่ง
        result = FindTaskByID(id)
        if result["from_id"] != userID:
            ReplyErrorTransaction(replyToken,Channel_Access_Token)
        else:
            reply = FlexInformation(result)
            ReplyTaskMessage(replyToken, reply, Channel_Access_Token)
    elif action == "check":         ## แสดงรายการงานรอตรวจ
        reply = FindReviewTask(userID)
        flexReply = FlexReviewTask(reply)
        ReplyTaskMessage(replyToken, flexReply, Channel_Access_Token)
    elif action == "ifcheck":     ## ตรวจงาน
        result = FindTaskByID(id)
        messageBack = BubbleAcceptRejectTask(result)
        ReplyTaskMessage(replyToken, messageBack, Channel_Access_Token)
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
    member = payload.get('member')
    typeWork = payload.get('type')
    detail = payload.get('detail')
    if subject == '' or userList == [] or detail == '' or typeWork == '' or deadline == '' :
        return 'Failed', 304
    else :
        deadline_obj = datetime.strptime(deadline,"%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(days=1)
        deadline_str = "{}/{}/{}".format(str(deadline_obj.day), str(deadline_obj.month), str(deadline_obj.year))

        userProfile = InsertNewTask(userList,member, subject, detail, typeWork, deadline_obj, userOrder, groupId)
        replyMessage = FlexDetailTask(subject, detail, deadline_str, member,userProfile )
        ReplyNewTask(groupId, replyMessage, userList, Channel_Access_Token)

        return 'Success',201
  
    