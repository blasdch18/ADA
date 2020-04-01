import numpy as np
import matplotlib.pyplot as plt
import random
from cmath import exp, pi

SAMPLE_RATE = 8192
N = 256	 # Windowing
 
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [exp( -2j*pi*k/N ) * odd[k] for k in range(N//2)]
    return [ even[k] + T[k] for k in range(N//2) ] + [ even[k] - T[k] for k in range(N//2)]
 

print( ''.join("%5.3f \n" % abs(f) 
                  for f in fft([11.0, 23.0, -4.0, 7.4, 5.0, 13.0, 21.0 ,17])) )
