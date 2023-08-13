import numpy as np

arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

media = 0
for i in arr:
    media+= i
media /= len(arr) 
print(media)

dp = 0
for i in arr:
    dp += (i - media)**2
dp = (dp/len(arr))**1/2
print(dp)