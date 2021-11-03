import pandas as pd
import matplotlib.pyplot as plt
import os
os.system("cls")
plt.style.use("seaborn")


x_axis = [1,2,3,4,5,6]
y_axis = [50,70,80,60,56,40]



plt.scatter(x_axis, y_axis, c="red",s=100, alpha=0.4)


plt.title("Scatter Plot")
plt.xlabel("Number of staff members")
plt.ylabel("Productivity in %")
plt.tight_layout()
plt.show()
