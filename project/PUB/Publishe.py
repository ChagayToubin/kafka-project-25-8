import json

from data import Data
from kafka import KafkaProducer


class Producer:
    def __init__(self):
        self.d = Data()
        self.interesting = self.d.data_loader_interesting()
        self.not_interesting = self.d.data_loader_not_interesting()
        self.producer = None

    def publish(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        self.intresthing_publish(self.interesting)

        self.not_intrsthing_publish(self.not_interesting)

        self.producer.close()

    def intresthing_publish(self, data):
        data = Producer.pop_first_items(data)
        for k, v in data.items():
            self.producer.send('interesting', {k: v})
            print("finsih send in")

    def not_intrsthing_publish(self, data):
        data = Producer.pop_first_items(data)
        for k, v in data.items():
            self.producer.send('not_interesting', {k: v})
            print("finish send not")

    @staticmethod
    def pop_first_items(d):
        new_dict = {}
        for key, lst in d.items():
            new_dict[key] = lst.pop(0)
        return new_dict
