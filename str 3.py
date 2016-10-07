__author__ = 'student'
import numpy as np
import random
import matplotlib.pyplot as plt

def get_percentile(values,bucket_number):
    x=100/bucket_number
    A=[0.0]
    for n in range(1,bucket_number):
        A.append(np.percentile(values,n*x))
    return A

def get_percentile_number(value, percentiles):
    A=0
    for n in range(len( percentiles)-1,0,-1):
        if (value >= percentiles[n]):
            A+=1
    return A
def value_equalization(value, percentiles,add_random):
    idx = get_percentile_number(value, percentiles)

    if not add_random :
        new_value = idx/len(percentiles)
    else:
        new_value = (idx + random.random())/len(percentiles)
    return new_value

def values_equalization(values, percentiles, add_random):
    for i in range(len(values)):
        values[i] = value_equalization(values[i], percentiles, add_random)
    return values


file_input = open('img.txt')

A = [[]*267]*200
for i in range (200):
    A[i] = list(map(float,file_input.readline().rstrip().split()))
data = np.array(A)

plt.subplot(221)
plt.imshow(data, cmap = plt.get_cmap('gray'))


plt.subplot(222)
b = data.flatten()
plt.hist(b, bins=10)


plt.subplot(223)
percentiles=get_percentile(b, 10)
new_data = np.array(values_equalization(data.flatten(),percentiles, False)).reshape((200, 267))
plt.imshow(new_data, cmap = plt.get_cmap('gray'))

plt.subplot(224)
b = new_data.flatten()
plt.hist(b, bins=10)





plt.show()