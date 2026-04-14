import numpy as np

a=np.array([1,2,3,4])
b=np.array([(1,1,1),(2,2,2)])
print(a);
print(b[0]);
print(a.dtype);

#array that crated the array of zeros
c=np.zeros((3,4))
print(c)

#array that creats the array of full of ones
d=np.ones((3,4))
print(d)

print(np.arange(10,20,2))
print(np.arange(0,10,2.5))
print(np.arange(12).reshape(4,3))

