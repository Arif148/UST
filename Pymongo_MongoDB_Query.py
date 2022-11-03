# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18

@author: ustpython02
"""

from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['pymongoDB']
    collection = db['transactions']
    
    # Run queries using pymongo on documents
    allDocuments = collection.aggregate([{ '$group' : 
                                          {'_id':'$category', 'averageAmount': 
                                          {'$avg':'$amount'}}}])
    #for item in allDocuments:
    #    print(item)
    
    # Q1. Display counts of each category in Transactions
    allDocuments = collection.aggregate([{'$group' : {'_id':'$category',
                                                    'totlaCount' : {'$count':{}}}}])
    #for item in allDocuments:
    #    print(item)
        
    
    # Q2. Display counts of each category in Transactions in descending order
    allDocuments = collection.aggregate([{'$group' : {'_id':'$category',
                                                    'totalCount' : {'$count':{}}}}, 
                                          {'$sort' : {'totalCount' : -1}}])
    #for item in allDocuments:
    #    print(item)
    
    # Q3. Display Top 5 trending products.
    allDocuments = collection.aggregate([{'$group' : {'_id':'$productname',
                                        'totalCount' : {'$count':{}}}}, 
                                          {'$sort' : {'totalCount' : -1}},
                                          {'$limit' : 5}])
    #for item in allDocuments:
    #    print(item)
        
    # Q4. Display Bottom 5 products by their sales.
    allDocuments = collection.aggregate([{'$group' : {'_id':'$productname',
                                        'totalCount' : {'$count':{}}}}, 
                                          {'$sort' : {'totalCount' : 1}},
                                          {'$limit' : 5}])
    for item in allDocuments:
        print(item)
