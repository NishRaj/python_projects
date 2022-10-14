import math
class Circle:
    def __init__(self,rad):
        self._rad_ = rad
    
   
    def area (self):
        return math.pi*(self._rad_**2)
