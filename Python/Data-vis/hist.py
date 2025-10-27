import numpy as np
import matplotlib.pyplot as plt

data=np.random.randn(1000)

plt.hist(data,bins=30,color='yellow',edgecolor='black')
plt.title('histogram charts')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
