import matplotlib.pyplot as plt
import os
import random


# Reading datasets
dir_path = os.path.dirname(os.path.realpath(__file__))
dataset = open(os.path.join(dir_path, "dataset.txt"),"r")



points = list()
for line in dataset.readlines():
    x_cord = line.split(" ")[0]
    y_cord = line.split(" ")[1]
    y_cord = y_cord.replace("\n","")
    points.append([x_cord, y_cord])


def kmeans(points, n_centers=0):
    centers = []
    centers_points = list()

    for i in range(n_centers):
        center = random.choice(points)
        if center not in centers:
            centers.append(center)

    print(centers)


    # for point in points: 
        


    return [[1,2],[[3,6,2,3,5],[7,5,5,2,4]]]





points = kmeans(points , 2)[1]


# plt.scatter(x,y, c="black", label="Group #1")

# plt.legend()
# plt.tight_layout()
# plt.grid()
# plt.show()


