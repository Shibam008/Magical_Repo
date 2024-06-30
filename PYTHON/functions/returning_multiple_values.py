import math

def circle_stats(radius):
   area = math.pi * radius ** 2
   circumference = 2 * math.pi * radius
   return area, circumference

area, circum = circle_stats(3)
print("Area : {:.2f}\nCircumference : {:.2f}".format(area, circum))