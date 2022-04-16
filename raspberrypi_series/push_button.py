import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
READ_PIN = 21
LED_PIN = 16
GPIO.setup(READ_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
READ_VAL = 0
try:
    while True:
        READ_VAL = GPIO.input(READ_PIN)
        print(READ_VAL)
        if READ_VAL != 0:
            GPIO.output(LED_PIN, True)
        else:
            GPIO.output(LED_PIN, False)
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()
