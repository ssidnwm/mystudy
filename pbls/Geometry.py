class Point:
    # your code here
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'A Point at ({},{})'.format(self.x,self.y)
    def __repr__(self):
        return 'Point at {},{}'.format(self.x,self.y)
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
class Square:
    def __init__(self,x):
        self.x = x
        self.y = x
    def __str__(self):
        return '{} X {} Square'.format(self.x,self.y)
    def __repr__(self):
        return 'Square {}'.format(self.x)
    def perimeter(self):
        return self.x * 4
    def area(self):
        return self.x * self.y
class Circle:
    def __init__(self,r=0):
        self.__radius = r
    def __str__(self):
        return 'A circle with a radius of {}cm'.format(self.__radius)
    def __repr__(self):
        return 'Circle ({})'.format(self.__radius)
    def radius(self):
        return self.__radius
    def diameter(self):
        return self.__radius*2
