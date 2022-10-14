import math
import code.Circle
class Circle:
    # pi = math.pi
    # @classmethod
    # def area_and_perimeter(cls,radius):
    #     area = cls.pi*(radius**2)
    #     perimeter = cls.pi*2*radius
    #     return area, perimeter
    def area (self):
        c = code.Circle.Circle(2)
        return c.area()
c1 = Circle()
print(c1.area())