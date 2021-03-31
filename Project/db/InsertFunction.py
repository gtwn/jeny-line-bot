from datetime import datetime,date
import pymongo
from pymongo import MongoClient
from Project.db.ConfigDB import *
from Project.Line.lineAPI import *
import pytz
import uuid



tasklistDB = db["tasks"]


def InsertNewTask(userList,member, subject, detail, typeWork, deadline, userOrderId, groupId):
    userProfile = GetUserProfile(userOrderId,Channel_Access_Token)
    groupName = GetGroupSummary(groupId, Channel_Access_Token)
    if typeWork == 'single':
        for u in userList:
            profile = GetUserProfile(u, Channel_Access_Token)
            data = {
                "task":     subject.strip(),
                "detail":   detail,
                "deadline": deadline,
                "created_at":datetime.now(),
                "done_at":  datetime.min,
                "order_by": userProfile,
                "from_id":  userOrderId,
                "group_id": groupId,
                "group_name": groupName,
                "type":     typeWork,
                "member":   [profile],
                "member_id": [u],
                "status":   "In Progress"
            }
            tasklistDB.insert_one(data)
    else:

        data = {
            "task":     subject.strip(),
            "detail":   detail,
            "deadline": deadline,
            "created_at":datetime.now(),
            "done_at":  datetime.min,
            "order_by": userProfile,
            "from_id":  userOrderId,
            "group_id": groupId,
            "group_name": groupName,
            "type":     typeWork,
            "member":   member,
            "member_id": userList,
            "status":   "In Progress"
        }
        tasklistDB.insert_one(data)

    return userProfile


