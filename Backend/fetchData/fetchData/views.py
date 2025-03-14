import requests
from django.http import JsonResponse
import csv
import json, redis


api_key= "579af2f50a3f2c8cf6fc4b1479917cc8f62babc3"

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': api_key
}


#FLOW
    #KAFKA-> REDIS->FLUTTER: current data
    #RECORDS->csv, CASSANDRA DB->SPARK->FLUTTER: historical data

#FOR DB UPDATES

def fetchLocData(request):
    url = f"https://api.waqi.info/feed/{loc}/?token={api_key}"
    response = requests.get(url, headers=headers)
    if(response.status_code != 200):
        return JsonResponse({"result": "error"})
    data = response.json()
    return cleanData(data)

def cleanData(data):
    location_value = data["data"]["city"]["name"]
    pm25_value = data["data"]["forecast"]["daily"]["pm25"]
    #print(location_value)
    if(pm25_value == []):
        return JsonResponse({"result": "pm25 values not found"})
    
    #storing in cassandra
    #sendToCassandra(location_value, pm25_value)

    #storing in csv
    with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date",  "location", "avg_pm25","max_pm25", "min_pm25"])
        for record in pm25_value:
            date = record["day"]
            avg_pm25 = record["avg"]
            max_pm25 = record["max"]
            min_pm25 = record["min"]
            writer.writerow([date,  location_value, avg_pm25, max_pm25, min_pm25])

    print("CSV file saved successfully!")
    return JsonResponse({"result": "success"})

#FOR FRONTEND  APP



#Records fetched from Spark->flutter
from django.http import JsonResponse
from .processData import fetchRecords   

def fetchrecords(request):
    data = fetchRecords()   
    return JsonResponse(data, safe=False)


#Current AQI data fetched from Kafka->redis->flutter

loc='hyderabad'

def sendtoApp(request):
    print('connected')
    url = f"https://api.waqi.info/feed/{loc}/?token={api_key}"
    response = requests.get(url)
    if(response.status_code != 200):
        return JsonResponse({"result": "error"})
    data = response.json()

    # return JsonResponse(data, safe=False)
    return sendToKafka((data))




# #kafka producer
from kafka import KafkaProducer
import json
import time
def sendToKafka(jsonData):
    producer = KafkaProducer(bootstrap_servers='kafkacont', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('currentData', value=jsonData)
    producer.flush() 
    print("Data sent to Kafka")
    return JsonResponse({"result": "data sent to Kafka"})





#read from Redis
def sendCurrentAQI(request):
    location = request.GET.get('location', 'hyderabad')
    redis_client = redis.StrictRedis(host='rediscont', port=6379, db=0, decode_responses=True)
    aqi_data = redis_client.get("Somajiguda, Hyderabad, India")
    
    if aqi_data:
        return JsonResponse({"aqi_data": json.loads(aqi_data)})
    else:
        return JsonResponse({"error": "No data found in Redis"})




