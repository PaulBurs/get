import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

data = np.loadtxt('data.txt')
settings = np.loadtxt('settings.txt')
disk = settings[1]
kvant = settings[0]
l = len(data)
time = l * disk
time_sar = np.argmax(data) * time / len(data)
x = [i * disk for i in range(l)]
y = [i * kvant for i in data]
fig, ax = plt.subplots(figsize = (16,10), dpi = 250)
ax.plot(x, y, color = 'g', label = 'Зависимость напряжения от времени', linewidth = 2)
ax.scatter(x, y, marker='s',c='blue',s=5)
ax.legend()
#title
ax.set_title('\n'.join(wrap('График зависимости напряжения на конденсаторе от времени')), loc = 'center')
plt.text(7,1.2, 'Время зарядки: ' + f"{round(time_sar,3)} с")
plt.text(7,1, 'Время разрядки: ' + f"{round(time - time_sar,3)} с")
#osi
ax.set_ylabel("Напряжение в вольтах")
ax.set_xlabel("Время в секундах")
plt.xticks(np.arange(0, max(x)+1, 1))
plt.yticks(np.arange(0, max(y) + 0.5, 0.5))
# включаем дополнительные отметки на осях
plt.minorticks_on()
plt.xlabel(r'$x$', fontsize=1)

#включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
fig.savefig('graf.svg')
plt.show()
