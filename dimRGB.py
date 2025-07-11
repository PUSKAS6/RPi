from vpython import *
import RPi.GPIO as GPIO
from time import sleep
dt=.1
rPin=37
gPin=35
bPin=33

rBut=11
gBut=13
bBut=15

rButState=1
rButStateOld=1
gButState=1
gButStateOld=1
bButState=1
bButStateOld=1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)

GPIO.setup(rBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bBut,GPIO.IN,pull_up_down=GPIO.PUD_UP)

myPWMr=GPIO.PWM(rPin,100)
myPWMg=GPIO.PWM(gPin,100)
myPWMb=GPIO.PWM(bPin,100)

DCr=0.9
DCg=0.9
DCb=0.9

myPWMr.start(int(DCr))
myPWMg.start(int(DCg))
myPWMb.start(int(DCb))

mySphere=sphere(color=color.red, radius=1)
try:
	while True:
		rate(20)
		rButState=GPIO.input(rBut)
		gButState=GPIO.input(gBut)
		bButState=GPIO.input(bBut)
		print('Button State',rButState,gButState,bButState)
		if rButState==1 and rButStateOld==0:
			DCr=DCr*1.58
			print('Red ok')
			if DCr>99:
				DCr=.9
		myPWMr.ChangeDutyCycle(int(DCr))
		if gButState==1 and gButStateOld==0:
			DCg=DCg*1.58
			print('Green ok')
			if DCg>99:
				DCg=.9
		myPWMg.ChangeDutyCycle(int(DCg))
		if bButState==1 and bButStateOld==0:
			DCb=DCb*1.58
			print('Blue ok')
			if DCb>99:
				DCb=.9
		myPWMb.ChangeDutyCycle(int(DCb))
		rButStateOld=rButState
		gButStateOld=gButState
		bButStateOld=bButState
		print(DCr,DCg,DCb)
		sleep(dt)
except KeyboardInterrupt:
	GPIO.cleanup()
	print()
	print('GPIO Good')
	print()

