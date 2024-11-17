import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

for i in range(10):
	GPIO.output(18, GPIO.HIGH)
	print("on")
	time.sleep(0.5)
	print("off")
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.5)

GPIO.cleanup()


