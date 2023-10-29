from publish import publish_to_topic, connect
import json
import time
import pandas as pd
import threading
import random

random_number = random.randint(100, 105)
df = pd.read_csv('generated_points.csv').head(random_number) 

topic = 'lightning/sensors'


#Create connection object
myAWSIoTMQTTClient = connect()


# Function for each thread to publish data
def publish_data_segment(start, end):
    for index in range(start, end):
        row = df.iloc[index]
        
        # Create the payload
        '''
        payload = {
            "DeviceID": int(row['DeviceID']),
            "Structure": {
                "Mount Type": None,
                "Tilt": None,
                "Degradation": None,
                "Estimated RUL": None
            },
            "Lightning": {
                "Lighting Element": None,
                "Model": None 
                "State": None,
                "Estimated RUL": None
            },
            "Weather": {
                "Temperature": None,
                "Humidity": None
            },
            "Solar": {
                "Solar Health": None,
                "Battery Health": None, 
                "Battery Charge": None,
                "Estimated RUL": None
            },
            "Location": {
                "Lat": row['Lat'],
                "Long": row['Long'],
                "Tag": row['Tag']
            },
            "Last Physical Inspection": None
            "Last Remote Inspection": None
            "Summary": None
        }
        '''

        payload = {
            "DeviceID": int(row['DeviceID']),
            "Tag": row['Tag'],
            "Lat": row['Lat'],
            "Long": row['Long'],
            "NodeType": "soft"
        }

        if random.random() <= 0.95:
            payload["Operation"] = "Normal"
        else:
            payload["Operation"] = "AN"


        # Publish the payload to AWS IoT
        publish_to_topic(myAWSIoTMQTTClient, topic, payload)


num_threads = 4 
chunk_size = len(df) // num_threads
thread_list = []

while True:
    # Create and start threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(df)
        thread = threading.Thread(target=publish_data_segment, args=(start, end))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    time.sleep(10)    

'''
try:
    publishToTopic(acc.myMQTTClient, topic, payload)
except:
    print("Error Occurred, could not publish one datapoint. Moving on...")

'''    
#installing packages 
#PS C:\Users\asogw\AppData\Local\Programs\Python\Python38\Scripts> .\pip.exe install pandas