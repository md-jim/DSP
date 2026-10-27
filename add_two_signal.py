import numpy as np
import matplotlib.pyplot as plt

n = np.arange(5)
x = np.array([1, 2, 3, 2, 1])
h = np.array([1, 1, 2, 1, 0])

y = x + h

print("Addition:", y)

plt.figure(figsize=(8, 5))

plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title("Signal x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h)
plt.title("Signal h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.title("Addition y[n] = x[n] + h[n]")
plt.xlabel("n")
plt.grid(True)

plt.tight_layout()
plt.show()