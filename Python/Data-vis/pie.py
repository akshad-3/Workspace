import matplotlib.pyplot as plt

country=['United States','Great Britain','China','Russia','Germany']
medal=[46,27,26,19,17]

plt.pie(medal,labels=country,autopct='%1.1f%%')
plt.title('pie chart')
plt.show()