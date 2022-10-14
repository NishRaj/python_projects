from curses import setupterm
from sys import settrace


class Student:
    all_students = []
    def __init__(self,name,grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        print("In Setter")
        if not 0 <= grade <= 100:
            raise ValueError("New Grade not in accepted range of [0,100]")
        self._grade = grade
    @staticmethod
    def calculate_average_grades(students) -> float:
        if len(students) < 1:
            return -1
        gradeSum=0
        for student in students:
            gradeSum += student.grade
        return gradeSum/len(students)
    @classmethod
    def get_average_grade(cls) -> float:
        return  cls.calculate_average_grades(cls.all_students)
    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) < 1:
            return None
        max_grade = 0
        best_student = None
        for student in cls.all_students:
            if student.grade >= max_grade:
                max_grade = student.grade
                best_student = student
        return best_student




stdlist = [Student('nishank',90),
           Student('Neha',95),
           Student('Abhyuday',96),
           Student('Nirvi',100)]
avgGrade = Student.calculate_average_grades(Student.all_students)
best_student = Student.get_best_student()
print(best_student.name)


