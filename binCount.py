import RPi.GPIO as GPIO
import time

LED1=37
LED2=35
LED3=33
LED4=31
LED5=29
ON=1
OFF=0
GPIO.setmode (GPIO.BOARD)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)

GPIO.output(LED1,0)
GPIO.output(LED2,0)
GPIO.output(LED3,0)
GPIO.output(LED4,0)
GPIO.output(LED5,0)
time.sleep(.5)

GPIO.output(LED1,1)
GPIO.output(LED2,0)
GPIO.output(LED3,0)
GPIO.output(LED4,0)
GPIO.output(LED5,0)
time.sleep(.5)

GPIO.output(LED1,0)
GPIO.output(LED2,1)
GPIO.output(LED3,0)
GPIO.output(LED4,0)
GPIO.output(LED5,0)
time.sleep(.5)

GPIO.output(LED1,1)
GPIO.output(LED2,1)
GPIO.output(LED3,0)
GPIO.output(LED4,0)
GPIO.output(LED5,0)
time.sleep(.5)
GPIO.output(LED1,0)
GPIO.output(LED2,0)
GPIO.output(LED3,1)
GPIO.output(LED4,0)
GPIO.output(LED5,0)
time.sleep(.5)
GPIO.cleanup()
