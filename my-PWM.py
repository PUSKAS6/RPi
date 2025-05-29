import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,True)
GPIO.output(37,False)
myPWM=GPIO.PWM(37,100)
myPWM.start(50)
