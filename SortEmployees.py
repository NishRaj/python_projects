def sort_employees(employees, sort_by): # name, age, salary
       new_employee_list = sorted(employees, key = lambda item : item[0] if sort_by == 'name' else (item[1] if sort_by == 'age' else item[2]))
       return new_employee_list

employees = [
    ["nishank",41, 100],
    ["neha",37, 200],
    ["abhyuday", 9, 100000],
    ["nirvi",1 , 200000],
    ["nirvi",2,200000]
]
print(sort_employees(employees, "name"))
