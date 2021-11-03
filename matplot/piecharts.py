import matplotlib.pyplot as plt
import os


os.system("cls")



print(plt.style.available)
plt.style.use("seaborn-deep")
slices = [40,60]
labels = ["Forty","Sixty"]
plt.pie(slices,labels=labels, wedgeprops={"edgecolor":"white"})


plt.title("Pie Chart")
plt.tight_layout()
plt.show()
