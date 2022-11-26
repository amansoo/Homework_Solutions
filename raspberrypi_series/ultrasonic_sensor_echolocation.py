import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig_pin = 23
echo_pin = 24
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN) # It is going to read where trig is on
#  or off hence input
try:
    while True:
        GPIO.output(trig_pin, 0)
        time.sleep(2E-6)
        GPIO.output(trig_pin, 1)
        time.sleep(10E-6)
        GPIO.output(trig_pin, 0)
        while GPIO.input(echo_pin) != 1:
            pass
        send_time = time.time()
        while GPIO.input(echo_pin) == 1:
            pass
        receive_time = time.time() # Divide this by 2 to get time of one journey
        travel_time = receive_time - send_time
        distance = 343 * (travel_time / 2) # s = vt
        print("The object is {}cm away from the sensor".format(round(distance * 100, 4)))
        # print("Ping took {} to travel".format(travel_time))
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIOs cleaned.")
