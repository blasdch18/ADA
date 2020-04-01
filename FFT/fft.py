import numpy as np

def FFT(x):
    # np
    x = np.asarray(x, dtype=float)
    # tamano de x
    N = x.shape[0]
    # print("x: ",x)
    if N % 2 > 0:
        raise ValueError("el tamano de 'x' tiene que ser potencia de 2")
    else:
        # separamos pares, impares hasta tamano 2
        if N>2:
            odd = FFT(x[0::2])
            even = FFT(x[1::2])
        else:
            odd = x[0]
            even = x[1]

        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        print ("T ->  ",factor)
        return np.concatenate([odd + factor[:N // 2] * even, odd - factor[:N // 2:] * even])

x = [11,23,-4,7.4,5,13,21,17]

print(x,'\n')

x = FFT(x)
n = np.arange(x.shape[0])




x = np.round(x,2)

print ('\n',x)