from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use("seaborn")


labels = ["Not Connected","Highly Satisfied","Differenciate Brand","Fully Connected"]
values = [18,36,49,88]

plt.bar(labels, values, bottom=-36, align='center', color=["#69cfff","#30bdff","#00aeff","#007cff"], width=0.4)

plt.title("Customer Values in Relation to Highly Satisfied Customers")
plt.ylabel("Customer Value")
plt.tight_layout()
plt.xticks(range(0,len(labels)),labels)
plt.show()

