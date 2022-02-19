########################################
########### Test DB cotent #############
########################################
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from pymongo import MongoClient

########################################
# upload data from both databases
def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df

########################################
# declare required data format


########################################
# check if data in correct format


########################################
# delete wrong entry
if errorDBHis > 0:
    DeleteErrorHis(errorEntry)

if errorDBRob > 0:
    DeleteErrorRob(errorEntry)


########################################
# save info about deleted entries in .txt file

