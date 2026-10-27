import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3,4])
h = np.array([1, 1,1,1])

y = np.convolve(x, h)

n_x = np.arange(len(x))
n_h = np.arange(len(h))
n_y = np.arange(len(y))

print("Linear Convolution:", y)

plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.stem(n_x, x)
plt.title("Input Signal x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n_h, h)
plt.title("Impulse Response h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n_y, y)
plt.title("Linear Convolution y[n]")
plt.xlabel("n")
plt.grid(True)

plt.tight_layout()
plt.show()