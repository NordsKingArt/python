import matplotlib.pyplot as plt


x = [1,5,6,8]
y = [4,3,6,3]

def kmeans(n_centers):
    # centers = {}
    # for i in range 
    # random.randint(0,len(x)-1)


    return [[1,2],[[3,6,2,3,5],[7,5,5,2,4]]]


center = kmeans(1)[0]
points = kmeans(1)[1]
plt.scatter(center[0],center[1], c="black", s=200)
plt.scatter(points[0],points[1], c="black", label="Group #1")

plt.legend()
plt.tight_layout()
plt.grid()
plt.show()


