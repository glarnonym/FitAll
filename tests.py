import myfitnesspal
from pymongo import MongoClient
import datetime
from datetime import date, timedelta
from datetime import datetime

clientMongo = MongoClient('mongodb+srv://kadoffel:%2BAllesRein%21@fitallcluster0-nfjp7.mongodb.net/test?retryWrites=true&w=majority')
db = clientMongo.FitAllDB.MFPal

clientMyfitnesspal = myfitnesspal.Client('arnonymg')

counter = 7

while (counter > 0):
    today = date.today() - timedelta(counter)
    day = clientMyfitnesspal.get_date(today)
    #todayWeight = clientMyfitnesspal.get_measurements('Weight', today)[today]
    try:
        todayCalories = day.totals['calories']
        if todayCalories < 1400:
            todayCalories = 0
    except KeyError:
        todayCalories = 0
    print(datetime.combine(today, datetime.min.time()))
    #print(todayWeight)
    print(todayCalories)
    print(clientMyfitnesspal.get_measurements('Fitbit steps'))
    counter = counter-1