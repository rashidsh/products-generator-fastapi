import argparse
import json
import random
import requests

from kafka import KafkaProducer
from pydantic import BaseSettings, KafkaDsn


class Settings(BaseSettings):
    kafka_url: KafkaDsn

    class Config:
        env_file = '.env'


def generate_product(sentence):
    return {
        'name': ' '.join(sentence.split()[:3]),
        'description': sentence,
        'sku': random.randint(1, int(2e9)),
        'price': random.randint(10, 10000),
    }


def main():
    settings = Settings()

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', metavar='N', type=int, default=100)
    args = parser.parse_args()

    producer = KafkaProducer(
        bootstrap_servers=settings.kafka_url.split('//')[1],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )

    res = requests.get('https://fish-text.ru/get', {
        'type': 'title',
        'number': 500,
        'format': 'json',
    }).json()
    if res['status'] != 'success':
        raise RuntimeError('API call failed')

    sentences = res['text'].split('\\n\\n')
    for _ in range(args.count):
        producer.send('new_product', generate_product(random.choice(sentences)))

    producer.flush()


if __name__ == '__main__':
    main()
