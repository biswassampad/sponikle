from pymongo import MongoClient

def connect_db():
     conn = MongoClient("mongodb://127.0.0.1:27017/sponikle")
        db = conn['aliedb']
        return db
