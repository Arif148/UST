# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:40:28 2022

@author: ustpython02
"""

from pymongo import MongoClient
import pandas as pd
import json

def mongoimport(csv_path, column_name):
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['pymongoDB']
    collection = db['transactions']
    # drop all documents
    collection.delete_many({})
    
    transaction_df = pd.read_csv(csv_path, names = column_name)

    payload = json.loads(transaction_df.to_json(orient = 'records'))
    collection.insert_many(payload)
    
    
    
column_name = ['_id', 'date', 'transaction_id', 'amount', 'category','productname', 
               'city', 'country', 'payment_details']
mongoimport('E:/IIHT-Bigdata/Data/transactions.csv', column_name)
