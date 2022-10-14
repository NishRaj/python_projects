import random

def contains (data, target):
    for item in data:
        if item == target:
            return True
    return False
lst = [1,2,3,4,5]
#print(contains(lst, 7))

def is_multiple(m,n):
    if m % n ==0:
        return True
    return False
#print(is_multiple(8,3))

def is_even(k):
    isEven = True;
    for i in range(1, k+1):
        if isEven == True:
            isEven = False
        else:
            isEven = True
    return isEven
#print(is_even(101))

def minmax(data):
    min = data[0]
    max = data[0]
    for number in data:
        if number <= min:
            min = number
        elif number > max:
            max = number
    return (min, max)
#print(minmax([4,-22,-33,1]))
def sum_of_squares(n):
    sum = 0
    for i in range(n):
      sum += (i+1)*(i+1)
    return sum
#print(sum_of_squares(2))
# def sum_of_squares_modified(n):
#     lst = []
#     for i in range(n):
#         lst[i] = (i+1)*(i+1)
#     return sum(lst)
# print(sum_of_squares_modified(1))
def addNum(firstNum, secondNum):
    result = firstNum + secondNum
    return result
#print(addNum(secondNum=4,firstNum=0))
def find_all_odds(lst):
    odd_list=[]
    for num in lst:
        if num%2!=0:
          odd_list.append(num)
    return odd_list
result = find_all_odds([-1,2,3,0,-5,6,7])
#print(result)
def string_lengths(strings):
    str_length= []
    for words in strings:
       str_length.append(len(words)) 
    return str_length
#print(string_lengths(["hello","blue","this","is","object"]))
def compare_lists(lst1=[], lst2=[]):
    # Write your code here.
    set1 = set(lst1)
    set2 = set(lst2)
    common_elem = set1.intersection(set2)
    return len(common_elem)
#print(compare_lists())
def trim_list(lst, elements_to_trim):
    trimmed_list = []
    for idx in range(len(lst) - elements_to_trim):
        element = lst[idx]
        trimmed_list.append(element)
    return trimmed_list
#print(trim_list([1,2,3,4,5],3))
def running_sums(numbers):
    # Write your code here.
    sum_list = [None]*len(numbers)
    sum_of_elements = 0
    for idx,elem in enumerate(numbers):
        sum_of_elements += elem
        sum_list[idx] = sum_of_elements
    return sum_list
#print(running_sums([5,4,2,1,5,6,4]))
def range_values():
    for range_val in range (50, 81, 10):
        print (range_val , end = "!!")
    for i in range(8,-9,-2):
        print(i, end = " ")
#range_values() 
def list_comp():
    list = [2**i for i in range (0,9)] # 1,2,4,8, 16, 32,64, 128, 256
    return list
#print(list_comp())

#print(random.choice([1,2,3,4,5,6]))
def customchoice(list : list) -> int:
   return list[random.randrange(0,len(list))]
print(type(customchoice([5,6,2,3,-1,-4])))

def searchForLetters(phrase:str, letters:str="aeoui") -> set:
    return set(letters).intersection(set(phrase))

def double(args):
    print('Before:', args)
    args.extend([5,6,7])
    print('After:', args)

#print(searchForLetters("Hi my name is Anthony Gonzalves"))
int_list = [1,2,3]
double(int_list)
print(int_list)