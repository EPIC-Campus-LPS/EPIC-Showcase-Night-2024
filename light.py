import RPI.GPIO as GPIO #Import the GPIO library so we can use the GPIO pins
import time #Import the time library so we can add time delays to our code

GPIO.setmode(GPIO.BCM) #Set the board mode of the GPIO pins so we can use the numbering on the Pi
GPIO.setwarnngs(False) #Set all warnings False to start 

GPIO.setup(18, GPIO.OUT) #Set 18 to be an output pin (as opposed to an input pin)

GPIO.output(18, GPIO.HIGH) #Set the output of 18 to high(turn on the pin)
time.sleep(5) #Wait for 5 seconds with the light on
GPIO.output(18, GPIO.LOW) #Set the output of 18 to low(turn off the pin)


GPIO.cleanup() #Turns all the pins off at the end
