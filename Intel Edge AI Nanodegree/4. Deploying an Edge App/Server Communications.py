# Import any libraries for MQTT and FFmpeg
import paho.mqtt.client as mqtt
import ffmpeg
import sys


#MQTT server environment variables
HOSTNAME = socket.gethostname()
IPADDRESS = socket.gethostbyname(HOSTNAME)
MQTT_HOST = IPADDRESS
MQTT_PORT = 3001
MQTT_KEEPALIVE_INTERVAL = 60

def infer_on_video(args, model):
    # Connect to the MQTT server
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)


            # Send the class names and speed to the MQTT server
            client.publish("class", json.dumps({"class_names": class_names}))
            client.publish("speedometer", json.dumps({"speed": speed}))

        # Send frame to the ffmpeg server
        sys.stdout.buffer.write(out_frame)
        sys.stdout.flush()

   
    # Disconnect from MQTT
    client.disconnect()

