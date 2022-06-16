class Vector:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __eq__(self, vector):
        return self.a == vector.a and self.b ==vector.b
    
    def __repr__(self):
        return f"Vector(a = {self.a}, b = {self.b})"
    
    def __add__(self,vector):
        new_a = self.a + vector.a
        new_b = self.b + vector.b
        return Vector(new_a, new_b)

    def __sub__(self, vector):
        new_a = self.a - vector.a
        new_b = self.b - vector.b
        return Vector(new_a, new_b)
    
    def __mul__(self,vector):
        prod_a = self.a * vector.a
        prod_b = self.b * vector.b
        dot_prod = prod_a + prod_b
        return dot_prod
         
v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1 - v2)