import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[3,4,6,2,9]

plt.plot(x,y,marker='o',linestyle='-',color='b')

plt.title("line chart")
plt.xlabel("x")
plt.ylabel("y")

plt.show()