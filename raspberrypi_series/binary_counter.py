import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
# Changes as the program progresses.
led_state_1 = 0
led_state_2 = 0
led_state_3 = 0
led_state_4 = 0
led_state_5 = 0
# All the rates are constant.
led_1_rate = 1
led_2_rate = 2
led_3_rate = 4
led_4_rate = 8
led_5_rate = 16
i_1 = 0
i_2 = 0
i_3 = 0
i_4 = 0
i_5 = 0

# My stroke of genius!
for i in range(0, 31):
    if i_1 == led_1_rate:  # Checks if the LED has waited long enough!
        if led_state_1 == 0:
            GPIO.output(17, 1)
            led_state_1 = 1
        else:
            GPIO.output(17, 0)
            led_state_1 = 0
        i_1 = 0
    
    if i_2 == led_2_rate:
        if led_state_2 == 0:
            GPIO.output(27, 1)
            led_state_2 = 1
        else:
            GPIO.output(27, 0)
            led_state_2 = 0
        i_2 = 0
    
    if i_3 == led_3_rate:
        if led_state_3 == 0:
            GPIO.output(26, 1)
            led_state_3 = 1
        else:
            GPIO.output(26, 0)
            led_state_3 = 0
        i_3 = 0

    if i_4 == led_4_rate:
        if led_state_4 == 0:
            GPIO.output(21, 1)
            led_state_4 = 1
        else:
            GPIO.output(21, 0)
            led_state_4 = 0
        i_4 = 0
    if i_5 == led_5_rate:
        if led_state_5 == 0:
            GPIO.output(20, 1)
            led_state_5 = 1
        else:
            GPIO.output(20, 0)
            led_state_5 = 0
        i_5 = 0
    
    i_1 += 1
    i_2 += 1
    i_3 += 1
    i_4 += 1
    i_5 += 1
    print(i_1, i_2, i_3, i_4, i_5)
    time.sleep(1  )
GPIO.cleanup()
