def sum_of_squares(n):
    sum = 0
    for i in range(n):
        sum += i*i
    return sum
print(sum_of_squares(3))

def sum_of_squares_comprehension(n):
    list = [i*i for i in range(n)]
    Sum = sum(list)
    return Sum
print(sum_of_squares_comprehension(3))

def sum_of_squares_odd_numbers(n):
    sum = 0
    for i in range(n):
        if i%2 !=0:
            sum += i*i
    return sum
print(sum_of_squares_odd_numbers(7))

def sum_of_squares_odd_numbers_comprehension(n):
    list = [i*i for i in range(n) if i%2 !=0]
    list_sum = sum(list)
    return list_sum
print(sum_of_squares_odd_numbers_comprehension(7))