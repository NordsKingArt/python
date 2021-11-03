import pandas as pd
import matplotlib.pyplot as plt
import os
os.system("cls")
plt.style.use("fivethirtyeight")



df = pd.read_csv("datasets/Salary_Data.csv")

years_experience = df["YearsExperience"]
salary = df["Salary"]


plt.plot(years_experience,salary, marker="o")
plt.fill_between(years_experience,salary, color="blue", alpha=0.2)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary by age")
plt.tight_layout()
plt.show()