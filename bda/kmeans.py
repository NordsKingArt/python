import matplotlib.pyplot as plt
import os
import random


# Reading datasets
dataset = open("bda/dataset.txt","r")

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


def map_points_to_centers(points, centers) : # Returns centers_points
    centers_points = dict()
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
    return centers_points


def reduce_centers(centers_points): # Returns new centers
    new_centers = list()
    for center_index in centers_points:
        points = centers_points[center_index]
        
        x_sum = 0
        y_sum = 0

        for point in points:
            x_sum+=int(point[0])
            y_sum+=int(point[1])

        new_centers.append([ round(x_sum/len(points),2), round(y_sum/len(points),2) ])

    return new_centers


def kmeans(points, n_centers=0):
    centers = list()
    centers_points = dict()

    while len(centers)<n_centers:
        center = random.choice(points)
        if center not in centers:
            centers.append(center)
    print(centers)


    while True:
        centers_points = map_points_to_centers(points, centers)
        new_centers = reduce_centers(centers_points)
        if(centers==new_centers):
            break
        print(f"{centers} are changed to {new_centers}")
        centers = new_centers

    # print(centers_points)
    for x in centers_points:
        print(f"Center {x} has {len(centers_points[x])} points")



    # for point in points: 
        


    return centers_points





points = kmeans(points , 6)[1]


# plt.scatter(x,y, c="black", label="Group #1")

# plt.legend()
# plt.tight_layout()
# plt.grid()
# plt.show()


