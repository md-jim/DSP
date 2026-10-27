import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-3, 4)
x = np.array([1, 2, 3, 4, 5, 2, 1])

x_reverse = x[::-1]

even = (x + x_reverse) / 2
odd = (x - x_reverse) / 2

print("Even component:", even)
print("Odd component:", odd)

plt.figure(figsize=(9, 6))

plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title("Original Signal x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, even)
plt.title("Even Component")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, odd)
plt.title("Odd Component")
plt.xlabel("n")
plt.grid(True)

plt.tight_layout()
plt.show()