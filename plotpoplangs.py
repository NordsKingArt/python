import matplotlib.pyplot as plt
import pandas as pd
import os
from collections import Counter
os.system("cls")


ages = [20,21,22,23,24,25,26,27,28,29,30]
languages = [10000,20000,30000,40000,20000,60000,30000,90000,20000,50000,30000]
plt.plot(ages,languages,marker="o")
plt.fill_between(ages,languages,)

# Config
plt.title("Number of Python users")
plt.xlabel("Ages")
plt.ylabel("# of programmers")
plt.style.use("seaborn")
plt.tight_layout()
plt.show()