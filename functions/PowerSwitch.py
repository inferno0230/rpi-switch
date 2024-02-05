import RPi.GPIO as GPIO
import time
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Class to control the power switch
class PowerSwitch:
    def __init__(self, command):
        self.command = command
        self.pin = 14
        if command == "hold":
            self.hold()
        else:
            self.singlePulse()
            
    def hold(self):
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()
        
    def singlePulse(self):
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()