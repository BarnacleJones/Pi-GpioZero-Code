from gpiozero import Button
from gpiozero import LED
from time import sleep

#globals
button = Button(12)
redLed = LED(26)
greenLed = LED(21)
gameOnBoi = True
redIsLit = False
greenIsLit = False
flashDuration = 0.2
resultFlashDuration = 0.02
#

#functions

def winner():
	for i in range(100):
		greenLed.on()
		sleep(resultFlashDuration)
		greenLed.off()
		sleep(resultFlashDuration)
		
def loser():
	for i in range(100):
		redLed.on()
		sleep(resultFlashDuration)
		redLed.off()
		sleep(resultFlashDuration)

def neither():
	for i in range(100):
		redLed.on()
		greenLed.on()
		sleep(resultFlashDuration)
		redLed.off()
		greenLed.off()
		sleep(resultFlashDuration)


def determineWinner(redIsLit):
	if redIsLit:
		print("Red was lit. Too bad.")
		loser()
	elif greenIsLit:
		print("WINNER")
		winner()
	else:
		print("Wow it was neither!")
		neither()
	
	
	
def gameStart():
	sleep(1)
	button.when_pressed = button_pressed_event	
	global redIsLit
	global greenIsLit
	while gameOnBoi:
		greenIsLit = False
		redLed.on()
		redIsLit = True
		sleep(flashDuration)
		redLed.off()
		redIsLit = False
		greenLed.on()
		greenIsLit = True
		sleep(flashDuration)
	#	greenLed.on()
	#	greenIsLit = True
	#	sleep(flashDuration)
		greenLed.off()
		greenIsLit = False
	determineWinner(redIsLit)

def button_pressed_event():
	global gameOnBoi
	global redIsLit
	global greenIsLit
	gameOnBoi = False
	

#
print("Press button to start. Try to click the button when the green LED is lit!")
button.wait_for_press()
gameStart()
