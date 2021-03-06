

import numpy as np
import matplotlib.pyplot as plt
import random

SAMPLE_RATE = 8192
N = 128 # Windowing



def fft_rec(X):
	N = len(X)

	if N <= 1:
		return

	even = np.array(X[0:N:2])
	odd = np.array(X[1:N:2])

	fft_rec(even)
	fft_rec(odd)

	for k in range(0, int(N/2)):
		t = np.exp(np.complex(0, -2 * np.pi * k / N)) * odd[k]
		X[k] = even[k] + t
		X[N/2 + k] = even[k] - t

def fft(x):
	X = list()
	for k in range(N):
		window = 1 # np.sin(np.pi * (k+0.5)/N)**2
		X.append(np.complex(x[k] * window, 0))

	fft_rec(X)
	return X



x_values = np.arange(0, N, 1)

x = np.sin((2*np.pi*x_values / 32.0)) # 32 - 256Hz
x += np.sin((2*np.pi*x_values / 64.0)) # 64 - 128Hz

X = fft(x)


# Plotting 
_, plots = plt.subplots(2)

## Plot in time domain
plots[0].plot(x)

## Plot in frequent domain
powers_all = np.abs(np.divide(X, N/2))
powers = powers_all[0:N/2]
frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N/2)), N)
plots[1].plot(frequencies, powers)


## Show plots
plt.show()