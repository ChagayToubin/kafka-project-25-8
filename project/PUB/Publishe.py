from data import Data
from kafka import KafkaProducer
import time

class Producer:
    def __init__(self):
       self.d=Data()

       self.ineresthing     = self.d.data_loader_interesting()
       self.not_ineresthing = self.d.data_loader_not_interesting()

    def publish(self):
        # יוצרים producer שמתחבר ל-broker מקומי
        producer = KafkaProducer(bootstrap_servers='localhost:9092')

        for i in range(5):
            message = f"שלום קפקא! הודעה {i}".encode('utf-8')
            producer.send('my-topic', message)  # שולחים ל-topic בשם "my-topic"
            producer.send('my-topic1', message)  # שולחים ל-topic בשם "my-topic"

            print("נשלח:", message.decode('utf-8'))
            time.sleep(1)

        producer.close()