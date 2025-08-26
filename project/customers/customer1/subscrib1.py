import pymongo
from kafka import KafkaConsumer
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["אהלן"]
mycol = mydb["interesting"]
datetime.now().strftime("%H:%M:%S")

consumer = KafkaConsumer(
    'interesting',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    print("messege", message.value.decode('utf-8'))

    mydict = {datetime.now().strftime("%H:%M:%S"):message.value.decode('utf-8')}

    x=mycol.insert_one(mydict)
    print("finsih enter to DB")
