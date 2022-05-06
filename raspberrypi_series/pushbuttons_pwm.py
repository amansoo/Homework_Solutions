import RPi.GPIO as GPIO
from time import sleep
led_pin = 16
yellow_button = 12
red_button = 17
# State pins
brightness = 1  # So that I know when the LED is supposed to be full OFF
yellow_button_old = 1
yellow_button_new = 1
red_button_old = 1
red_button_new = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
my_pwm = GPIO.PWM(led_pin, 60)
my_pwm.start(brightness)
print(brightness)
# Configuring the pushbuttons witht he internal pull up resistor.
GPIO.setup(yellow_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        yellow_button_new = GPIO.input(yellow_button)
        red_button_new = GPIO.input(red_button)
        if yellow_button_old == 0 and yellow_button_new == 1:
            if brightness == 97:
                my_pwm.ChangeDutyCycle(99)
                brightness = 97
                print(brightness)
            else:
                brightness += 8
                print(brightness)
                my_pwm.ChangeDutyCycle(brightness)    
        if red_button_old == 0 and red_button_new == 1:
            if brightness == 1:
                my_pwm.ChangeDutyCycle(0)
                brightness = 1
                print(brightness)
            else:
                brightness -= 8
                print(brightness)
                my_pwm.ChangeDutyCycle(brightness)
        yellow_button_old = yellow_button_new
        red_button_old = red_button_new
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("All good")
