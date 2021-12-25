import matplotlib.pyplot as plt
import math


x = []
y = []
for a in range(-100, 100, 1):
    if a != 0:
        x.append(a)
        y.append(1/math.sin(a))
plt.plot(x, y)
plt.show()
