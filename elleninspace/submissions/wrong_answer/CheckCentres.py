import math
import time


n = int(input())

spaceStationCoordinates = []

for _ in range(n):
    (x,y,z) = map(float, input().split())
    spaceStationCoordinates.append((x,y,z))


projections = []

for station in spaceStationCoordinates:
    x, y, z = station
    vy = math.atan(z/x)
    vx = math.atan(y/x)
    
    d = math.sqrt((x**2)+(y**2)+(z**2))
    vr = math.asin(1/d) #radius is 1
    projections.append((vx, vy, vr))


focuspoints = []

for circle in projections:
    x1, y1, r1 = circle
    focuspoints.append((x1,y1))


maxIntersections = 0
for point in focuspoints:
    intersections = 0
    x1,y1 = point
    for circle in projections:
        x2,y2,r = circle
        if(abs(x1-x2)**2+abs(y1-y2)**2 <= (r+1*10**-9)**2): #Compare distance, without having to compute square root
            intersections += 1
    if(intersections > maxIntersections):
        maxIntersections = intersections

print(maxIntersections)

