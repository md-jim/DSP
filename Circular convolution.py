import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
h = np.array([1, 1, 2, 2])

N = len(x)
y = np.zeros(N)

for n in range(N):
    for k in range(N):
        y[n] += x[k] * h[(n - k) % N]

print("Circular Convolution:", y)

plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.stem(np.arange(N), x)
plt.title("Signal x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(N), h)
plt.title("Signal h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(np.arange(N), y)
plt.title("Circular Convolution (Circle Method)")
plt.xlabel("n")
plt.grid(True)

plt.tight_layout()
plt.show()