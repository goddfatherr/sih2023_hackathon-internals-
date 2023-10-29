from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

def connect():
   

    #Configure connection parameters 
    endpoint                = "a2zkd5mbjhq66z-ats.iot.eu-west-1.amazonaws.com"
    port                    = 8883
    device_cert_path        = "./certs/certificate.crt"
    private_key_cert_path   = "./certs/private_key.key"
    root_auth_cert_path     = "./certs/root_cert.pem"

    # For certificate based connection
    myAWSIoTMQTTClient = AWSIoTMQTTClient("client1")

    # For TLS mutual authentication
    myAWSIoTMQTTClient.configureEndpoint(endpoint, 8883) 
    myAWSIoTMQTTClient.configureCredentials(root_auth_cert_path, private_key_cert_path, device_cert_path) 


    # AWSIoTMQTTClient connection configuration
    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    myAWSIoTMQTTClient.connect()
    
    print("Client Connected")
    return myAWSIoTMQTTClient


def disconnect():
    MQTTClient_Obj.disconnect()
    print("Client Connected")


def publish_to_topic(myAWSIoTMQTTClient, topic, payload):
    payload_str = json.dumps(payload)
    myAWSIoTMQTTClient.publish(topic, payload_str, 0)  
    print(payload['DeviceID'])