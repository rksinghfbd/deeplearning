import numpy as np

a = np.array([1,2,3,4,5])
print(a)

import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()

c = np.dot(a,b)

toc = time.time()
print (c)
print ("Vectorized version:" + str(1000*(toc-tic)) + "ms")

c = 0;
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
    
toc = time.time()
print (c)
print ("Non-vectorized version:" + str(1000*(toc-tic)) + "ms")


a = np.array([[1,2,3],[4,5,6], [7,8,9],[1,1,1]])
b = np.array([[1],[1],[1],[1]])

print (a.shape)
print (b.shape)

c =  a + b
 
print (c)

