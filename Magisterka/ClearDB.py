########################################
############### Clear DB ###############
########################################

########################################
# Function to delete all entries in DB_his

def DeleteAllDocsHis(self,myquery):
    #if action stop delete all documents from collection from baza_robocza
    #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #mydb = myclient["mydatabase"]
    #mycol = mydb["customers"]

    x = mycol.delete_many({})

    print(x.deleted_count, " documents deleted.")


########################################
# Function to delete all entries in DB_rob

def DeleteAllDocsRob(self,myquery):
    #if action stop delete all documents from collection from baza_robocza
    #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #mydb = myclient["mydatabase"]
    #mycol = mydb["customers"]

    x = mycol.delete_many({})

    print(x.deleted_count, " documents deleted.")


########################################
# Function to delete one entry in DB_his

def DeleteErrorHis(self,myquery):
    # check data correctness with data format example
    #if data format wrong, delete this document
    #myquery = { "address": "Mountain 21" }

    mycol.delete_one(myquery)

########################################
# Function to delete one entry in DB_rob

def DeleteErrorRob(self,myquery):
    # check data correctness with data format example
    #if data format wrong, delete this document
    #myquery = { "address": "Mountain 21" }

    mycol.delete_one(myquery)