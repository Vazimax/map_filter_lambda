import math

# First method to calculate the area :

def area(r):
    return math.pi * pow(r,2)

raduis = [8.47,3,6,1.1]

# areas = []

# for i in raduis:
#     x = area(i)
#     areas.append(x)

# print(areas)

# Second one :

output2 = list(map(area,raduis))
print(output2)

