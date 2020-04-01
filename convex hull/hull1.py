import numpy as np
import matplotlib.pyplot as plt
import pdb

def divide(u, v, points):
    return [p for p in points if np.cross(p - u, v - u) < 0]
    
def extend_div(u, v, points):
    if not points:
        return []

    w = min(points, key=lambda p: np.cross(p - u, v - u))
    print("......................W ........................")
    print(w)
    print(divide(w, v, points)) 
    print("================================================")
    print(divide(u, w, points))

    p1 = divide(w, v, points)
    p2 = divide(u, w, points)

    print("-----------------extend---------------------")
    print(extend_div(w, v, p1),extend_div(u, w, p2))
    return extend_div(w, v, p1) + [w] + extend_div(u, w, p2)

def convex_hull(points):

    u = min(points, key=lambda p: p[0])
    print(">>>>>>>>>>>>>>>>>min<<<<<<<<<<<<<<<<<")
    print(u)
    v = max(points, key=lambda p: p[0])
    print(">>>>>>>>>>>>>>>>>max<<<<<<<<<<<<<<<<<")
    print(v)

    left =divide(u, v, points)
    right =divide(v, u, points)

    print("++++++++++++++++++++++++++++++++left:")
    print(left)
    print("++++++++++++++++++++++++++++++++right:")
    print(right)

    return [v] + extend_div(u, v, left) + [u] + extend_div(v, u, right) + [v]

points = np.random.randint(20,size=(10,2))
for x in points:
	print(x)
hull = np.array(convex_hull(points))
#hullnumpy

plt.plot(points[:, 0],points[:, 1] ,'.')
plt.plot(hull[:, 0],hull[:, 1] ,'-' )


plt.show()

