import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

pwm = GPIO.PWM(24, 1000)
pwm.start(0)

try:
    while True:
        coeff = int(input("Enter coefficient"))
        pwm.ChangeDutyCycle(coeff)
        print(3.3 * coeff / 100)

finally:
        pwm.stop()
        GPIO.output(24, 0)
        GPIO.cleanup()