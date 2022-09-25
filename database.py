from pymongo import MongoClient
import logging

class ClientDB:
    def __init__(self, con_string):
        self.con_string = con_string
        self.logger = logging.getLogger(__name__)

    def connect(self):
        self.client = MongoClient(self.con_string)
        self.logger.info("Connected to the DB")

    def printstuff(self):
        collection = self.client.test1.test
        cursor = collection.find({})
        for document in cursor:
            print(document)
    
