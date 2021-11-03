import matplotlib.pyplot as plt

x = [1,2,2,3,4]
y = [1,1,2,3,3]


plt.scatter(x,y, label="Ps")


plt.scatter(2,0)
plt.scatter(3,2)

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()