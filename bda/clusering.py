import random

from pyspark.sql.types import NullType

class KMeans():

    def __init__(self, points, n_centers):
        self.points = points
        self.n_centers = n_centers

    def calculate_euler_distance(self, point1, point2):
        point1, point2 = [int(point1[0]),int(point1[1])],[int(point2[0]),int(point2[1])]
        distance = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) ** 0.5
        return distance


    def map_points_to_centers(self, points, centers) : # Returns centers_points
        centers_points = dict()
        for point in points:
            min_distance = self.calculate_euler_distance(centers[0], point)
            min_center = 0
            for index, center in enumerate(centers):
                distance = self.calculate_euler_distance(center, point)
                if distance < min_distance:
                    min_distance = distance
                    min_center = index
            if min_center not in centers_points:
                centers_points[min_center] = list()
            centers_points[min_center].append(point)
        return centers_points


    def reduce_centers(self, centers_points): # Returns new centers
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


    def cluster(self):
        centers = list()
        centers_points = dict()

        while len(centers)<self.n_centers:
            center = random.choice(self.points) # Generates Random centers
            if center not in centers:
                centers.append(center)

        print(f"Random centers are: {centers} \n")


        while True:
            centers_points = self.map_points_to_centers(self.points, centers)
            new_centers = self.reduce_centers(centers_points)
            if(centers==new_centers): break # No Change, Halt
            print(f"{centers} are changed to {new_centers} \n")
            centers = new_centers

        # print(centers_points)
        for x in centers_points:
            print(f"Center {x} has {len(centers_points[x])} points")

        return centers_points
