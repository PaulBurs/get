import RPi.GPIO as GPIO
import time
def dec_bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def bin_led(value):
    for i in range(8,0,-1):
        if 2**i - 1 <= value:
            return dec_bin(2**i - 1)
    return dec_bin(0)

def adc(troyka):
    
    value = 0
    for i in range(7, -1, -1):
        
        GPIO.output(dac, dec_bin(value + 2**i))
        time.sleep(0.0008)
        if GPIO.input(comp) == 0:
            value += 2**i

    return value



GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH) 
GPIO.setup(comp, GPIO.IN)



try:
    while True:
        GPIO.output(led, bin_led(adc(troyka)))
        
        
        
finally:
    GPIO.output(led,[0]*8)

GPIO.output(led,[0]*8)
GPIO.cleanup()
