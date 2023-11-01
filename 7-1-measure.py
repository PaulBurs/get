import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import json
#Задаю пины для работы
DAC = [8,11,7,1,0,5,12,6]
comp=14
troyka=13
leds = [2,3,4,17,27,22,10,9]
#Настраиваю пины для работы
GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=0)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(leds,GPIO.OUT)
GPIO.output(DAC,0)
#перевод из 10 в 2 систему
def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
    
#значение на адц
def sar_adc():
    bin_val=[0,0,0,0,0,0,0,0]
    for i in range(0,8):
        bin_val[i]=1
        GPIO.output(DAC,bin_val)
        time.sleep(0.003)
        if GPIO.input(comp)==1:
            bin_val[i]=0
    return int(''.join([str(i) for i in bin_val]), base=2)

data=[]
stage=0
max_v_rasbery=3.3
max_V= (2.67 /max_v_rasbery)*(2**8-1)

step_adc=max_v_rasbery/(2**8-1)

#основная часть
try:
    GPIO.output(troyka,1)
    start=time.time()
    while(True):

        value=sar_adc()
        data.append(value)
        num_leds=int((sar_adc())/256 * 8)
        GPIO.output(leds, [0]*(8-num_leds) + [1]*num_leds)

        #зарядка конденсатора
        if(stage == 0):
            print('Заряжаем конденсатор и проводим измерения')
            if(value >= (max_V*0.97)):
                stage += 1
                GPIO.output(troyka,0)

        #разрядка конденсатора
        elif(stage == 1):
            print('Разряжаем конденсатор и проводим измерения')
            if(value <= (max_V*0.9)):
                end = time.time()
                stage += 1

        #завершение эксперимента
        else:
            print('Записываем данные в файл, сохранаяем настройки и выводим данные на экран')
            plt.plot(range(len(data)),data,"o")
            time = end-start
            disk = len(data)/time
            print(len(data))
            with open('data.txt','w') as f:
                for i in data:
                    f.write(str(i) + "\n")

            with open('settings.txt','w') as f:
                s = str(disk) + " " + str(step_adc)
                f.write(s)

            print(f"Эксперимент длился: {round(time,4)} сек")
            print(f"Одно измерение длилось: {round(1/disk,4)} сек")
            print(f"Средняя частота дискретизации: {round(disk,1)} Гц")
            print(f"Шаг квантования: {round(step_adc,4)} В/шаг")
            plt.show()
            break

finally:
    print('Завершаем программу, подачей на все пины 0, а также очистки настроек')
    GPIO.output(DAC,0)
    GPIO.output(leds,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()