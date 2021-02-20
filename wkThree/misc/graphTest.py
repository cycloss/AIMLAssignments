import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-2, 2, 100)
print(xs[:5])
print(xs[-5:])
ys = [x**3 - 2 * x for x in xs]

plt.plot(xs, ys)
plt.grid()
plt.axhline(y=0, lw=1, color='k')
plt.axvline(x=0, lw=1, color='k')
plt.show()

plt.plot(xs, np.array(ys) * 5)
plt.grid()
plt.axhline(y=0, lw=1, color='g')
plt.axvline(x=0, lw=1, color='b')
plt.show()
