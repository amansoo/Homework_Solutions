import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
print("Welcome to How-Many_Blinks! Enter 0 at any time to quit!")
while True:
    blinks = int(input("How many blinks do you want, sir?\n"))
    if blinks == 0:
        break
    for i in range(0, blinks):  # I'm not using blinks + 1, because I am starting at 0 and
    # 1
        GPIO.output(11, True)
        time.sleep(0.5)
        GPIO.output(11, False)
        time.sleep(0.5)

GPIO.cleanup()  # Always cleanup your mess! (Pro-tip ;-))
