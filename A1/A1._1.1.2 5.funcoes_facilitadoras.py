import numpy as np

arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])
elementos_organizados = arr
elementos_organizados.sort()
print(elementos_organizados)

print(arr.shape)

print(arr.mean())
print(arr.std(), arr.max(), arr.min())

from numpy import random
arr_aleatoria = random.randint(11, size=(100))
print(arr_aleatoria)
