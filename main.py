from functions.MqttService import MqttService
import time
mqtt_service = MqttService()

if __name__ == "__main__":
    try:
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Exiting gracefully")
        mqtt_service.client.loop_stop()
        mqtt_service.client.disconnect()
        exit(0)