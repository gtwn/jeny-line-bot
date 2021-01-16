from Project.Config import *
import pymongo
from pymongo import MongoClient


uri = "mongodb+srv://{}:{}@cluster0-aarl2.mongodb.net/{}?retryWrites=true&w=majority".format(DB_Username,DB_Password,DB_Name)
cluster = pymongo.MongoClient(uri)

db = cluster["{}".format(DB_Name)]
