import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec_to_bin(x):
    digits = [0,0,0,0,0,0,0,0]
    for i in range(8):
        digits[7-i] = x % 2
        x = int(x / 2)
    return digits

inc_f = 1
ti = 0
ex = 0

try:
    T = float(input("Enter period: "))

    while True:
        GPIO.output(dac, dec_to_bin(ex))
        if ex == 0:
            inc_f = 1
        elif ex == 255:
            inc_f = 0
        ex = ex + 1 if inc_f == 1 else ex - 1

        time.sleep(T/512)
        ti += 1

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

