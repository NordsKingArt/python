from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use("seaborn")

ages = range(17,26)
salaries = [500,600,700,800,900,1000,1500,1600,1700]

plt.title("Salaries by age")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.plot(ages,salaries, linewidth="2", marker="o", label="All Salaries")


# plt.grid()
plt.legend()
plt.show()