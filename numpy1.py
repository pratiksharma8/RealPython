import numpy as np

a = np.zeros((5, 5))
print(a)

b = np.array([1, 2, 3])
c = np.array([4, 5, 6])
d = np.sum((b, c), axis=0)
e = np.sum((b, c), axis=1)
print(d)
print(e)

x = np.array([12, 43, 3, 200, 102, 32, 56])
y = x[np.argsort(x)[-2:][::-1]]
print(y)

