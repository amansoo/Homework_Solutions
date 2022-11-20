import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D22)
mcp = MCP.MCP3008(spi, cs)
red = AnalogIn(mcp, MCP.P0)
green = AnalogIn(mcp, MCP.P1)
blue = AnalogIn(mcp, MCP.P7)

GPIO.setup(21, GPIO.OUT)
red_pwm = GPIO.PWM(21, 120) # pin, frequency
red_pwm.start(100) # duty cycle

GPIO.setup(20, GPIO.OUT)
green_pwm = GPIO.PWM(20, 120) # pin, frequency
green_pwm.start(100) # duty cycle

GPIO.setup(16, GPIO.OUT)
blue_pwm = GPIO.PWM(16, 120) # pin, frequency
blue_pwm.start(100) # duty cycle

try:
    while True:
        red_raw = round(red.voltage, 2)
        red_8bit = 99 / 3.3 * red_raw
        green_raw = round(green.voltage, 2)
        green_8bit = 99 / 3.3 * green_raw
        blue_raw = round(blue.voltage, 2)
        blue_8bit = 99 / 3.3 * blue_raw
        red_pwm.ChangeDutyCycle(red_8bit)
        green_pwm.ChangeDutyCycle(green_8bit)
        blue_pwm.ChangeDutyCycle(blue_8bit)
        print("Red {}\nGreen {}\nBlue {}\n".format(red_8bit, green_8bit, blue_8bit))
except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIOs cleaned")
