import math


class Polygon:
   def get_area() -> float:
    raise NotImplementedError("Area is not implemented")
   
   def get_perimeter() -> int:
    raise NotImplementedError("Perimeter is not implemeneted")


class Triangle(Polygon):
    
    def __init__(self, side1, side2, side3) -> None:
       self.side1 = side1
       self.side2 = side2
       self.side3 = side3
    def get_sides(self) -> list:
        return [self.side1, self.side2, self.side3]
    def get_area(self) -> float:
       semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
       return math.sqrt(
        semi_perimeter *
        (semi_perimeter - self.side1) *
        (semi_perimeter - self.side2) *
        (semi_perimeter - self.side3)
    )

class Rectangle(Polygon):
    def __init__(self,width, height) -> None:
       self.height = height
       self.width = width
    
    def get_sides(self) -> list:
        return [self.width, self.height, self.width, self.height]
    
    def get_area(self) -> float:
        return self.width*self.height

class Square(Rectangle):
   def __init__(self, side):
    super().__init__(side,side)
    self.side = side
   

s = Square(4)
print(s.get_area())
print(s.get_sides())
