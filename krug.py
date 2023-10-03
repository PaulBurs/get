import matplotlib.pyplot as plt
x = [i for i in range(-100,101)]
y = [(100**2 - a**2)**0.5 for a in x]
for b in x:
    y.append(-((100**2 - b**2)**0.5))
for c in range(100,-101,-1):
    x.append(c)


plt.plot(x, y, label='linear', marker='o', linestyle='-', color='red', linewidth=1)

plt.show()
plt.show()
plt.savefig('test.png')