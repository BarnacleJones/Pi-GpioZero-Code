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
flashDuration = 0.05
#

#functions

def winner():
	for i in range(10):
		greenLed.on()
		sleep(flashDuration)
		greenLed.off()
		sleep(flashDuration)
		
def loser():
	for i in range(10):
		redLed.on()
		sleep(flashDuration)
		redLed.off()
		sleep(flashDuration)


def determineWinner(redIsLit):
	if redIsLit:
		print("Red was lit. Too bad.")
		loser()
	else:
		print("WINNER")
		winner()
	
	
	
def gameStart():
	sleep(1)
	button.when_pressed = button_pressed_event	
	global redIsLit
	global greenIsLit
	while gameOnBoi:
		redLed.on()
		redIsLit = True
		sleep(flashDuration)
		redLed.off()
		redIsLit = False
		sleep(flashDuration)
		greenLed.on()
		greenIsLit = True
		sleep(flashDuration)
		greenLed.off()
		greenIsLit = False
		sleep(flashDuration)
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
