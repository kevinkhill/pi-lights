import RPi.GPIO as GPIO
import time

RELAY_PIN = 23

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    
def cleanup():
    GPIO.cleanup()

def on():
    GPIO.output(RELAY_PIN, False)

def off():
    GPIO.output(RELAY_PIN, True)

def pulse(duration):
    on()
    time.sleep(duration)
    off()
