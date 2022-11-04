from  pymongo import MongoClient
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_flight(csv_path):
    flight_data=pd.read_csv(csv_path)
    fl_data=json.loads(flight_data.to_json(orient='records'))
    collection.delete_many({})

    collection.insert_many(fl_data)

if __name__=="__main__":
    print("welcome to pymongo")
    client=MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['airline_delayDB']
    collection=db['flights']
    read_flight('D:\python trianings\Assignment 4 on Pymongo_Flight_Delay\Flights_Delay.csv')

# b). Average arrival delay caused by airlines
avg_delay=collection.aggregate([   {'$group': {'_id':'$AIRLINE','total_avg': { '$avg':'$ARRIVAL_DELAY'}}}  ])                              

# c). Days of months with respect to average of arrival delays. [Create a suitable plot using matplotlib/seaborn]
day_avg_delay=collection.aggregate([   {'$group': {'_id':'$DAY','total_avg': { '$avg':'$ARRIVAL_DELAY'}}}  ])

# d). Arrange weekdays with respect to the average arrival delays caused. [Create a suitable plot using matplotlib/seaborn]
day_week=collection.aggregate([   {'$group': {'_id':'$DAY_OF_WEEK','total_avg': { '$avg':'$ARRIVAL_DELAY'}}}  ])

# e). Arrange Days of month as per cancellations done in descending order.  [Create a suitable plot using matplotlib/seaborn]
day_cancel=collection.aggregate([
    {'$match':{'CANCELLED':1}},
     {'$group': {'_id': '$DAY','day_counts': { '$count':{}}}},
     {'$sort':{'DAY':-1}}])

# f). Find the busiest airports with respect to day of week. Create a suitable plot using matplotlib/seaborn.
busy_airport=collection.aggregate([
    {'$group': {'_id': '$ORIGIN_AIRPORT', 'max_day' : { '$max' : '$DAY_OF_WEEK'}}},{'$sort':{'max_day':-1}},{'$limit':1}])

# g). Find top 10 Airlines of US. Create a suitable plot using matplotlib/seaborn.
top_airlines=collection.aggregate([
    {'$match':{'AIRLINE':'US'}},
     {'$group': {'_id': 'null'}},
     {'$sort':{'AIRLINE':-1}},
     {'$limit':10},{'$project':{'_id':0}}])

# h). Finding airlines that make the maximum, minimum number of cancellations.
can_max_min=collection.aggregate([
    {'$group': {'_id': 'null', 'max cancelation' : { '$max' : '$CANCELLED'},
                                'min cancelation' : { '$min' : '$CANCELLED'}}} ,
    {'$project':{'_id':0}}])

# i). Find and show airlines names in descending that make the most number of diversions made. [Create a suitable plot using matplotlib/seaborn]
diversion=collection.aggregate([  
                                {'$match':{'DIVERTED':1}},
                                {'$group': {'_id':'$AIRLINE','total_counts': { '$count':{}}}},
                                {'$sort':{'total_counts':-1}} ])

# j). Finding days of month that see the most number of diversion
day_diversion=collection.aggregate([   {'$group': {'_id':'$AIRLINE','total_counts': { '$count':{}}}},
                                    {'$sort':{'total_counts':-1}} ])
# k). Calculating mean and standard deviation of departure delay for all flights in minutes

# l). Calculating mean and standard deviation of arrival delay for all flights in minutes

# m). Create a partitioning table “flights_partition” using partitioned by schema “CANCELLED”

# n). Finding all diverted Route from a source to destination Airport & which route is the most diverted route.

# o). When is the best time of day/day of week/time of a year to fly with minimum delays?




for item in   top_airlines:
     print(item)
#plt.plot(flight_data['alldoc_c'])

