import RPi.GPIO as GPIO
from time import sleep

read_pin = 12
led_pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(read_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

button_state_old = 1 # In a pull-up resistor configurstion, this means
GPIO.output(led_pin, 0)
led_state = 0
# button is not held

try:
    while True:
        button_state_new = GPIO.input(read_pin)
        if button_state_old == 0 and button_state_new == 1:
            if led_state == 0:
                GPIO.output(led_pin, 1)
                led_state = 1
            elif led_state == 1:
                GPIO.output(led_pin, 0)
                led_state = 0
        button_state_old = button_state_new
        sleep(0.15)
except KeyboardInterrupt:
    GPIO.cleanup()
