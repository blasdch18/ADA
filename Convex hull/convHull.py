import numpy as np
import matplotlib.pyplot as plt
import pdb
from random import randint 

def create_points(ct,min=0,max=50):
	return [[randint(min,max),randint(min,max)] for _ in range(ct)]


def scatter_plot(coords,convex_hull=None):
	xs,ys=zip(*coords) # unzip into x and y coord lists
	plt.scatter(xs,ys,) # plot the data points

	if convex_hull!=None:

		for i in range(1,len(convex_hull)+1):
			if i==len(convex_hull): i=0 # wrap
			c0=convex_hull[i-1]
			c1=convex_hull[i]
			plt.plot((c0[0],c1[0]),(c0[1],c1[1]),'r')
	plt.show()


def min_max_x(pts):
    minX = pts[0].X
    maxX = pts[0].X
    minXPoint = pts[0]
    maxXPoint = pts[0]
    for pt in pts:
        if pt.X < minX:
            minX = pt.X
            minXPoint = pt
        if pt.X > maxX:
            maxX = pt.X
            maxXPoint = pt
    cor = [minXPoint, maxXPoint]
    return cor

def PointSide(point, line):
	sp = line.StartPoint
	ep = line.EndPoint
	d = (point.X - sp.X) * (ep.Y - sp.Y) - (point.Y - sp.Y)*(ep.X - sp.X)
	if d > 0:
		return 1
	elif d == 0:
		return 0
	else:
		return -1

def PointsRightSide(points, line):
    ret = []
    for pt in points:
        if (PointSide(pt, line)) > 0:
            ret.append(pt)
    return ret

def PointsLeftSide(points, line):
    ret = []
    for pt in points:
        if (PointSide(pt, line)) < 0:
            ret.append(pt)
    return ret
def PointFarthest(points, line):
    if len(points) == 0:
        return None
    far = points[0]
    for pt in points:
        if pt.DistanceTo(line) > far.DistanceTo(line):
            far = pt
    return far;

def MainTriangles(point, line):
    if point is None:
        return None
    return Polygon.ByPoints([line.StartPoint, point, line.EndPoint])

def GetRestOfPoints(polygon, points):
    if polygon is None:
        return None
    restOfPoints = []
    for point in points:
        if not Polygon.ContainmentTest(polygon, point) and not polygon.DoesIntersect(point):
            restOfPoints.append(point)
    return restOfPoints

def GetNextPointRight(line, points):
    ptsRight = PointsRightSide(points, line)
    farPointRight = PointFarthest(ptsRight, line)
    mainTriangleRight = MainTriangles(farPointRight, line)
    restOfPoints = GetRestOfPoints(mainTriangleRight, ptsRight)

    if len(ptsRight) == 0:
        return line
    r1 = GetNextPointRight(Line.ByStartPointEndPoint(line.StartPoint, farPointRight), restOfPoints)
    r2 = GetNextPointRight(Line.ByStartPointEndPoint(farPointRight, line.EndPoint), restOfPoints)

    return [r1, r2]

def GetNextPointLeft(line, points):
    ptsRight = PointsLeftSide(points, line)
    farPointRight = PointFarthest(ptsRight, line)
    mainTriangleRight = MainTriangles(farPointRight, line)
    restOfPoints = GetRestOfPoints(mainTriangleRight, ptsRight)

    if len(ptsRight) == 0:
        return line
    r1 = GetNextPointLeft(Line.ByStartPointEndPoint(line.StartPoint, farPointRight), restOfPoints)
    r2 = GetNextPointLeft(Line.ByStartPointEndPoint(farPointRight, line.EndPoint), restOfPoints)

    return [r1, r2]

def quick(pts):
    #determining points with min and max X coordinate
    minXPoint, maxXPoint = min_max_x(pts)
    #creating line between these points
    lineMinMaxX = Line.ByStartPointEndPoint(minXPoint, maxXPoint)
    #determining points on right and left side
    ptsRight = PointsRightSide(pts, lineMinMaxX)
    ptsLeft = PointsLeftSide(pts, lineMinMaxX)
    resultRight = GetNextPointRight(lineMinMaxX, ptsRight)
    resultLeft = GetNextPointLeft(lineMinMaxX, ptsLeft)

    w =[resultLeft , resultRight]

    return w

#points= create_points(100)
points=[[9,6],[5,5],[1,4],[3,3],[5,2],[3,1],[0,0],[7,0]]    

print(points)
hull=quick(points)
print(hull)
scatter_plot(points,hull)


