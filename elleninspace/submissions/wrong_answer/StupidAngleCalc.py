import math

def get2Ddist(x1,y1,x2,y2):
    return math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)

#https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles
def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return (x3, y3, x4, y4)

n = int(input())

spaceStationCoordinates = []

for _ in range(n):
    (x,y,z) = map(float, input().split())
    spaceStationCoordinates.append((x,y,z))


projections = []

for station in spaceStationCoordinates:
    x, y, z = station
    vy = 0 if z == 0 else math.atan(y/z) #Honestly, IDK what i was thinking here, but we once though this was correct, so worth testing for
    vx = math.atan(y/x)
    
    d = math.sqrt((x**2)+(y**2)+(z**2))
    vr = math.asin(1/d) #radius is 1
    projections.append((vx, vy, vr))


focuspoints = []

for circle in projections:
    x1, y1, r1 = circle
    focuspoints.append((x1,y1))
    for otherCircle in projections:
        x2, y2, r2 = otherCircle
        intersections = get_intersections(x1,y1,r1, x2,y2,r2)
        if(intersections):
            i1x, i1y, i2x, i2y = intersections
            focuspoints.append((i1x, i1y))
            focuspoints.append((i2x, i2y))


maxIntersections = 0
for point in focuspoints:
    intersections = 0
    x1,y1 = point
    for circle in projections:
        x2,y2,r = circle
        if(get2Ddist(x1,y1,x2,y2) <= r+1*10**-9):
            intersections += 1
    if(intersections > maxIntersections):
        maxIntersections = intersections

print(maxIntersections)
