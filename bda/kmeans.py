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


def calculate_euler_distance(point1, point2):
    point1, point2 = [int(point1[0]),int(point1[1])],[int(point2[0]),int(point2[1])]
    distance = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) ** 0.5
    return distance


def kmeans(points, n_centers=0):
    centers = list()
    centers_points = dict()

    for i in range(n_centers):
        center = random.choice(points)
        if center not in centers:
            centers.append(center)


    for point in points:
        min_distance = calculate_euler_distance(centers[0], point)
        min_center = 0
        for index, center in enumerate(centers):
            distance = calculate_euler_distance(center, point)
            if distance < min_distance:
                min_distance = distance
                min_center = index
        if min_center not in centers_points:
            centers_points[min_center] = list()
        centers_points[min_center].append(point)
    print(centers_points)


    # for point in points: 
        


    return [[1,2],[[3,6,2,3,5],[7,5,5,2,4]]]





points = kmeans(points , 2)[1]


# plt.scatter(x,y, c="black", label="Group #1")

# plt.legend()
# plt.tight_layout()
# plt.grid()
# plt.show()


