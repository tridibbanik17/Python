import math
import random

d = float(input("Enter the distance to the nearest zombie in meters: "))

g = 9.81

theta = float(random.random() * 45)

theta_rads = math.radians(theta)

v = math.sqrt(g * d / math.sin(2 * theta_rads))

print("Ready for launch!")
print("Set angle to ", theta, " degrees")
print("Set speed to ", v, " m/s")
