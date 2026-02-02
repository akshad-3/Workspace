import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y,color="red",linewidth=2,label="line")

plt.xlabel("x")
plt.ylabel("y")
plt.title("tile")

plt.legend()

plt.show()
