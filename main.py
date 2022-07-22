# Distance Calculator Using Python
import math


def calc_distance(x1, y1, x2, y2):
    math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# INPUT
x1 = int(input("Please enter the x-value of the first point: "))
y1 = int(input("Please enter the y-value of the first point: "))
x2 = int(input("Please enter the x-value of the second point: "))
y2 = int(input("Please enter the y-value of the second point: "))

# PROCESS


def calc_distance(x1, y1, x2, y2):
    math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


distance = calc_distance(x1, y1, x2, y2)

# OUTPUT
print("The distance between the two points is " + str(distance) + ".")
