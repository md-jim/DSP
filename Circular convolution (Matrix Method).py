import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
h = np.array([1, 2, 1, 0])

N = len(x)

H = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        H[i, j] = h[(i - j) % N]

y = H @ x

print("Circular Convolution Matrix:")
print(H)

print("Circular Convolution:", y)

plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.stem(np.arange(N), x)
plt.title("Input Signal x[n]")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(N), h)
plt.title("Input Signal h[n]")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(np.arange(N), y)
plt.title("Circular Convolution (Matrix Method)")
plt.xlabel("n")
plt.grid(True)

plt.tight_layout()
plt.show()