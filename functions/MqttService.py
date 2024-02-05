import os
import paho.mqtt.client as mqtt
from functions.PowerSwitch import PowerSwitch
import dotenv

class MqttService:
    def __init__(self):
        dotenv.load_dotenv()
        self.broker_address = os.getenv("MQTT_BROKER_ADDRESS")
        self.broker_port = int(os.getenv("MQTT_BROKER_PORT"))
        self.username = os.getenv("MQTT_USERNAME")
        self.password = os.getenv("MQTT_PASSWORD")
        self.topic = os.getenv("MQTT_TOPIC")

        # Create an instance of the PowerSwitch class
        self.relay_controller = PowerSwitch()

        # Create an MQTT client instance
        self.client = mqtt.Client()

        # Set the callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Set username and password for MQTT authentication
        self.client.username_pw_set(self.username, self.password)

        # Connect to the MQTT broker
        self.client.connect(self.broker_address, self.broker_port, 60)

        # Start the MQTT loop
        self.client.loop_start()

    # Callback when the connection to the broker is established
    def on_connect(self, client, userdata, flags, rc):
        # Subscribe to the topic when connected
        client.subscribe(self.topic)

    # Callback when a message is received from the broker
    def on_message(self, client, userdata, msg):
        message = msg.payload.decode("utf-8")

        if message.lower() == "switchhold":
            # Code to keep the switch on for 5 seconds
            self.relay_controller.hold()
        elif message.lower() == "switchpulse":
            # Code to emulate a power switch press
            self.relay_controller.singlePulse()
