class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0
    
    '''
    This is a property getter and setter properties.
    '''
    @property 
    def salary(self):
        print("Run getter")
        return round(self._salary)
    @salary.setter
    def salary(self, salary):
        print("Run setter")
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary

p1 = Person("Nishank")
p1._salary = -100
print(p1._salary)

