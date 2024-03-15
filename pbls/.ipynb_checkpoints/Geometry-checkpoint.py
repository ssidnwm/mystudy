
class Point:
    # your code here
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def halfway(self,p):
        return Point((self.x+p.x)/2,(self.y+p.y)/2)
    def midpoint(p,q):
        return Point((p.x+q.x)/2,(p.y+q.y)/2)
    def reflect_x(self):
        return Point(self.x,-self.y)
    def reflect_y(self):
        return Point(-self.x,self.y)
    def slope_to_origin(self):
        return self.y/self.x
