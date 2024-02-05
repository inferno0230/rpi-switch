import RPi.GPIO as GPIO
import time

# Class to control the power switch
class PowerSwitch:
    def __init__(self):
        self.pin = 21

    def hold(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()
        
    def singlePulse(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()
