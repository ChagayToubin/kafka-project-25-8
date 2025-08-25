from kafka import KafkaConsumer

# יוצרים consumer שמאזין ל-topic
consumer = KafkaConsumer(
    'my-topic1',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # מתחילים לקרוא מהתחלה
    group_id='my-group'            # קבוצה של צרכנים
)

print("מקשיב להודעות...")

for message in consumer:
    print("התקבלה הודעה:", message.value.decode('utf-8'))
