import RPi.GPIO as GPIO
from time import sleep
dt=.1
rPin=37
gPin=35
bPin=33

rbut=11
gbut=13
bbut=15

rButState=1
rButStateOld=1

gButState=1
gButStateOld=1

bButState=1
bButStateOld=1

rLEDstate=0
gLEDstate=0
bLEDstate=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)

GPIO.setup(rbut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gbut,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(bbut,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
		rButState=GPIO.input(rbut)
		gButState=GPIO.input(gbut)
		bButState=GPIO.input(bbut)
		
		print('Button States',rButState,gButState,bButState)
		if rButState==1 and rButStateOld==0:
			print('Red OK')
			rLEDstate= not rLEDstate
			GPIO.output(rPin,rLEDstate)
		if gButState==1 and gButStateOld==0:
                        print('Green OK')
                        gLEDstate= not gLEDstate
                        GPIO.output(gPin,gLEDstate)
		if bButState==1 and bButStateOld==0:
                        print('Blue OK')
                        bLEDstate= not bLEDstate
                        GPIO.output(bPin,bLEDstate)
		rButStateOld=rButState
		gButStateOld=gButState
		bButStateOld=bButState
                
                
		sleep=dt
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GPIO gOOD TO gO')
