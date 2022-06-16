import math
class Circle:
    pi = math.pi
    @classmethod
    def area_and_perimeter(cls,radius):
        area = cls.pi*(radius**2)
        perimeter = cls.pi*2*radius
        return area, perimeter

print(Circle.area_and_perimeter(4))   
