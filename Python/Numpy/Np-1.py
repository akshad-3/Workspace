import numpy as np

a=np.array([1,2,3,4])
b=np.array([(1,1,1),(2,2,2)])
print(a);
print(b[0]);
print(a.dtype);

c=np.zeros((3,4))
print(c)

#array that creats the array of full of ones
d=np.ones((3,4))
print(d)

print(np.arange(10,20,2))
print(np.arange(0,10,2.5))
print(np.arange(12).reshape(4,3))

E=np.array([[1,2,3,4,5],[1,2,3,4,5]])
F=np.array([[1,2,3,4,5],[1,2,3,4,5]])

print(E*F)

