import matplotlib.pyplot as plt
import os

plt.style.use("seaborn-deep")
os.system("cls")

timeline = [1,2,3,4,5,6]
player1 = [0,2,4,3,6,7]
player2 = [5,3,9,3,4,2]
player3 = [5,6,3,6,8,10]

plt.stackplot(timeline, player1, player2, player3, labels=["Aking","Erik","Jaker"])

plt.tight_layout()
plt.legend(loc=(0.08,0.05))
plt.show()