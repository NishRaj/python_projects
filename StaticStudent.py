class Student:
    grace = 2.0
    def __init__(self, name,grades=[]):
        self.grades = grades
        self.name = name
    
    @classmethod
    def average_grades(cls,grades):
        print("class")
        return (sum(grades) + cls.grace)/len(grades)
    
    @staticmethod
    def average_grades(grades):
        print("static")
        return sum(grades)/len(grades)

std = Student('Nishank',[65,75,35])
print(Student.average_grades(std.grades))