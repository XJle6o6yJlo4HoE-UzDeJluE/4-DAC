import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec_to_bin(x):
    digits = [0,0,0,0,0,0,0,0]
    # digits = list(map(int, str(format(x, 'b'))))
    for i in range(8):
        digits[7-i] = x % 2
        x = int(x / 2)
    return digits

try:
    while True:
        dnum = input("Enter your decimal number:")
        if dnum == "q":
            break
        dnum = int(dnum)
        if 0 <= dnum <= 255:
            array = range(8)
            array = dec_to_bin(dnum)
            GPIO.output(dac, array)
            volt = float(dnum) / 256.0 * 3.3
            print(f"Voltage: {volt} volt")
        else:
            print("Error.")
    

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


    