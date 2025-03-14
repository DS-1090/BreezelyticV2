import time
from kafka import KafkaConsumer
import json, redis

def fetchFromKafka():
    while True:  
        try:
            consumer = KafkaConsumer(
                'currentData',
                bootstrap_servers='kafkacont:9092',
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                auto_offset_reset='earliest',
                group_id="aqi_group"
            )

            redis_client = redis.StrictRedis(host='rediscont', port=6379, db=0, decode_responses=True)

            print("Listening from kafka Producer")

            for message in consumer:
                data = message.value
                city_name = data.get("data", {}).get("city", {}).get("name", "unknown")
                redis_client.set(city_name, json.dumps(data))
                print("Stored in Redis")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5) 

fetchFromKafka()
