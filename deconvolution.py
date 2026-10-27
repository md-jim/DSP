import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import deconvolve

x = np.array([1, 2, 3])
h = np.array([1, 1])

y = np.convolve(x, h)

recovered, remainder = deconvolve(y, h)

print("Convolved Signal:", y)
print("Recovered Signal:", recovered)
print("Remainder:", remainder)

plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(y)), y)
plt.title("Convolved Signal y[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(len(h)), h)
plt.title("Known Signal h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(np.arange(len(recovered)), recovered)
plt.title("Recovered Signal x[n]")
plt.xlabel("n")
plt.grid(True)

plt.tight_layout()
plt.show()