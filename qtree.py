import numpy as np
import matplotlib.pyplot as plt

class Point: #Point-Evaluation

    def __init__(self, x, y):
        self.x, self.y = x, y

class Box: #Bound-Evaluation

    def __init__(self, centralx, centraly, width, height):
        self.cx, self.cy = centralx, centraly
        self.width, self.height = width, height
        self.west_edge, self.east_edge = centralx - width/2, centralx + width/2
        self.north_edge, self.south_edge = centraly - height/2, centraly + height/2

    def checkcondition(self, point):

        try:
            point_x, point_y = point.x, point.y
        except AttributeError:
            point_x, point_y = point

        return (point_x >= self.west_edge and point_x <  self.east_edge and point_y >= self.north_edge and point_y < self.south_edge)

    def draw(self, ax):
        x1, y1 = self.west_edge, self.north_edge
        x2, y2 = self.east_edge, self.south_edge
        ax.plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1])


class Tree: #Tree-construciton

    def __init__(self, boundary, max_points=2, depth=1):
        
        self.boundary = boundary
        self.max = max_points
        self.points = []
        self.depth = depth
        self.divided = False

    def divide(self):

        cx, cy = self.boundary.cx, self.boundary.cy
        width, height = self.boundary.width / 2, self.boundary.height / 2

        self.nw = Tree(Box(cx - width/2, cy + height/2, width, height), self.max, self.depth + 1)

        self.ne = Tree(Box(cx + width/2, cy + height/2, width, height), self.max, self.depth + 1)

        self.se = Tree(Box(cx + width/2, cy - height/2, width, height), self.max, self.depth + 1)

        self.sw = Tree(Box(cx - width/2, cy - height/2, width, height), self.max, self.depth + 1)
        self.divided = True

    def draw(self, ax):

        self.boundary.draw(ax)
        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.se.draw(ax)
            self.sw.draw(ax)

    def insert(self, point):

        if not self.boundary.checkcondition(point):
            return False
        
        if len(self.points) < self.max:
            self.points.append(point)
            return True

        if not self.divided:
            self.divide()

        return (self.ne.insert(point) or self.nw.insert(point) or self.se.insert(point) or self.sw.insert(point))

#Body
    

width, height = 1000, 1000 #Size

N = 500 #Particle-count

coords = np.random.randn(N, 2) * height/2 + (width/2, height/2)
points = [Point(*coord) for coord in coords]
domain = Box(width/2, height/2, width, height)
qtree = Tree(domain, 1)

for point in points:
    qtree.insert(point)

#Plot

fig = plt.figure()
ax = plt.subplot()
ax.set_xlim(0, width)+ (width/2, height/2)
ax.set_ylim(0, height)
qtree.draw(ax)
ax.scatter([p.x for p in points], [p.y for p in points], s=4)

plt.show()

    

