import numpy as np

a = np.random.randn(5)
print(a)
print (a.shape)

b = np.random.randn(5,1)
print (b)
print (b.T)
print(np.dot(b,b.T))


a = np.random.randn(12288,150)
b = np.random.randn(150, 45)

c = np.dot(a,b)

print(c.shape)

