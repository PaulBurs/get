import RPi.GPIO as GPIO
import time
def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def adc(troyka):
    m = [0]
    for value in range(256):
        GPIO.output(dac, dec_bin(value))
        time.sleep(0.00001)

        if GPIO.input(comp) == 0:
            m.append(value)
    return m[-1]



GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH) 
GPIO.setup(comp, GPIO.IN)



try:
    while True:
        print(dec_bin(adc(troyka)), "{:.4f}".format(adc(troyka) / 256 * 3.3) + " В")
        
        
        
finally:
    GPIO.output(dac,[0]*8)

GPIO.output(dac,[0]*8)
GPIO.cleanup()
