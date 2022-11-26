# Program to control a servo motor with a potentiometer using
# an MCP3008 to read analogIn() values.
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import RPi.GPIO as GPIO
import time
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D22)
mcp = MCP.MCP3008(spi, cs)
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(2)
pot = AnalogIn(mcp, MCP.P1)
try:
    while True:
        # test has been conducted, converting first to 255 then
        # mapping that to servo dc is better than mapping
        # raw voltage to servo dc
        raw_vol = pot.voltage
        bit8 = round((255 / 3.3) * raw_vol) # First map to 8 bit form
        dc = (10 / 255) * bit8 + 2 # Then map to duty cycle for the servo with the 8 bit form
        servo_pwm.ChangeDutyCycle(dc)
        print("Raw: {}, 8 bit: {}, DC: {}".format(raw_vol, bit8, dc))
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIOs cleaned.")
  