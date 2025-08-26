from kafka import KafkaConsumer
from pymongo import MongoClient


# יוצרים consumer שמאזין ל-topic
consumer = KafkaConsumer(
    'interesting',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # מתחילים לקרוא מהתחלה
    group_id='my-group'            # קבוצה של צרכנים
)


for message in consumer:
    print("messege", message.value.decode('utf-8'))
    print(type( message.value.decode('utf-8')))

    client = MongoClient("mongodb://admin:1234@localhost:27017/")

    mydb = client["אהלן אהלן"]
    mycol = mydb["interesting"]

    mydict = {"name": "John", "address": "Highway 37"}

    x = mycol.insert_one(mydict)