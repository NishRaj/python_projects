class Employee:
    average_age = 0
    average_salary = 0
    count = 0
    def __init__(self, name,age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        total_age = Employee.average_age*Employee.count
        total_salary = Employee.average_salary*Employee.count
        Employee.count +=1
        Employee.average_age =  (total_age + age)/Employee.count
        Employee.average_salary = (total_salary + salary)/Employee.count

employee1 = Employee("Tim", 10, 65000)
employee2 = Employee("Clement", 23, 10000)
employee3 = Employee("Conner", 45, 15000)
print(Employee.average_age,Employee.average_salary)