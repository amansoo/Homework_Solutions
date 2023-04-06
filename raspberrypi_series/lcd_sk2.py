# we use pyserial in this library because the DHT11
# temperature sensor does not work with my raspberry pi
# for some reason. We use an ESP32 in this project but
# that can be substituted with an arduino if need be.
import LCD1602
import time
import serial
import RPi.GPIO as GPIO
def convert(t, unit):
    if unit == " C": # meaning convert to F
        conv = str(round((float(t) * 9/5) + 32, ndigits=2))
    if unit == " F": # meaning convert to C
        conv = temp_hum_list[0]
    return conv
arduino_object = serial.Serial('/dev/ttyACM0')
time.sleep(1)
LCD1602.init(0x27, 1)
switch = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
old = 0
#GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
unitT = " C"
try:
    while True:
        while (arduino_object.inWaiting() == 0):
            pass
        new = GPIO.input(switch)
        print(old, new)
        # geetting the data from the serial port
        arduino_data = arduino_object.readline()
        arduino_data = str(arduino_data, 'utf-8') # cleaning data
        arduino_data = arduino_data.strip('\r\n')
        
        temp_hum_list = arduino_data.split(" ") # separating tem and hum
        temp, hum = temp_hum_list # note: temp and hum are strings!
        if unitT == " F":
            temp = convert(temp, " C")
        if (old == 1 and new == 0):
            if unitT == " C":
                temp = convert(float(temp), unitT)
                unitT = " F"
            elif unitT == " F":
                temp = convert(float(temp), unitT)
                unitT = " C"
        
        temp += unitT
        hum += " %"
        LCD1602.write(0, 0, "Tem: {}".format(temp))
        LCD1602.write(0, 1, "Hum: {}".format(hum))
        print(temp, hum)
        old = new
except KeyboardInterrupt:
    time.sleep(1)
    LCD1602.clear()
    GPIO.cleanup()
    print("LCD cleaned")
