import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(5*x)

def find_peaks(A):
    peaks = []
    indices = []
    for n in range(len(A)-1):
        if (A[n] > A[n+1]) and (A[n] > A[n-1]):
            peaks.append(A[n])
            indices.append(n)
    return peaks, indices


y_peaks, indices = find_peaks(y)
x_peaks = x[indices]
plt.plot(x, y)
plt.scatter(x_peaks, y_peaks)
plt.show()


