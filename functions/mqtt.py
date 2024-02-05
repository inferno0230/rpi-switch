import time
import paho.mqtt.client as mqtt
#from  import PowerSwitch

# Replace these with your MQTT broker's details
broker_address = "mqtt.broker.com"
broker_port = 1883
topic = "relay/control"
username = "your_username"
password = "your_password"

# Create an instance of the PowerSwitch class
relay_controller = PowerSwitch()

# Callback when the connection to the broker is established
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic when connected
    client.subscribe(topic)

# Callback when a message is received from the broker
def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print(f"Received message: {message}")

    if message == "hold":
        # Code to keep switch on for 5 seconds
        relay_controller.hold()
    elif message == "pulse":
        # Code to emulate a power switch press
        relay_controller.singlePulse()

# Create an MQTT client instance
client = mqtt.Client()

# Set the callbacks
client.on_connect = on_connect
client.on_message = on_message

# Set username and password for MQTT authentication
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT loop
client.loop_start()

try:
    # Keep the script running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Disconnect gracefully on Ctrl+C
    client.disconnect()
    print("Disconnected from MQTT broker")
