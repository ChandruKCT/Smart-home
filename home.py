from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
import time

app = Flask(__name__)

 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

@app.route('/fan_on')
def fan_on():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	return 'Fan on'

@app.route('/fan_off')
def fan_off():
	GPIO.output(Motor1E,GPIO.LOW)

	return 'Fan off'

@app.route('/lights_on')
def lights_on():
	GPIO.output(12,GPIO.HIGH)

	return 'Lights on'

@app.route('/lights_off')
def lights_off():
	GPIO.output(12,GPIO.LOW)

	return 'Lights off'

@app.route('/door_open')
def door_open():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT)
	pwm=GPIO.PWM(11,50)
	pwm.start(5)
	pwm.ChangeDutyCycle(5)
	time.sleep(1.5)

	return 'Door open'

@app.route('/door_close')
def door_close():	
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT)
	pwm=GPIO.PWM(11,50)
	pwm.start(5)
	pwm.ChangeDutyCycle(10)
	time.sleep(1.5)

	return 'Door close'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)



