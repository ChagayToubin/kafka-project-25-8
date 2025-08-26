from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'not_interesting',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    print("התקבלה הודעה:", message.value.decode('utf-8'))
