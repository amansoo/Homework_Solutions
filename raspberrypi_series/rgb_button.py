import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
# pins
red_channel = 26
green_channel = 19
blue_channel = 13
red_button = 12
green_button = 20
blue_button = 16
# setup
GPIO.setup(red_channel, GPIO.OUT)
GPIO.setup(green_channel, GPIO.OUT)
GPIO.setup(blue_channel, GPIO.OUT)
GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blue_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# states
red_state = 0
green_state = 0
blue_state = 0
red_button_old = 1
red_button_new = 1
green_button_old = 1
green_button_new = 1
blue_button_old = 1
blue_button_new = 1
# loop
try:
    while True:
        red_button_new = GPIO.input(red_button)
        green_button_new = GPIO.input(green_button)
        blue_button_new = GPIO.input(blue_button)
        if red_button_new == 1 and red_button_old == 0:
            red_state = not red_state
            GPIO.output(red_channel, red_state) 
        if green_button_new == 1 and green_button_old == 0:
            green_state = not green_state
            GPIO.output(green_channel, green_state)
        if blue_button_new == 1 and blue_button_old == 0:
            blue_state = not blue_state
            GPIO.output(blue_channel, blue_state)
        
        red_button_old = red_button_new
        green_button_old = green_button_new
        blue_button_old = blue_button_new
        sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO reset.")
