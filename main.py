# Distance Calculator Using Python

import math

# INPUT
x1 = int(input("Please enter the x-value of the first point: "))
y1 = int(input("Please enter the y-value of the first point: "))
x2 = int(input("Please enter the x-value of the second point: "))
y2 = int(input("Please enter the y-value of the second point: "))

# PROCESS
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# OUTPUT
print("The distance between the two points is " + str(distance) + ".")
