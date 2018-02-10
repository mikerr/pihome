from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)


# LED across 26 and GND (bottom 2 pins, long LED pin on 26)
GPIO.setup(26,GPIO.OUT)


while True:

	GPIO.output(26,1)
	time.sleep(1)

	GPIO.output(26,0)
	time.sleep(1)

GPIO.cleanup()
