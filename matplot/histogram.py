import pandas as pd
import matplotlib.pyplot as plt
import os
os.system("cls")
plt.style.use("fivethirtyeight")


ages = [10,15,16,17,19,25,30,40,60]
bins = [11,20,30,40,50,60]

plt.hist(ages,bins=bins, edgecolor="silver")



plt.title("Histogram")
plt.tight_layout()
plt.show()