for i in range(10):
    print("Hello")
for i in range(5,10):
    print(i)
# Iterate through index on a list
lst = [1,2,3,4,5,6,True, False]
for idx in range(0,len(lst)):
    print(lst[idx])

#Iterate through the elements
for elements in lst:
    print(elements)

#Enumerate
for i, element in enumerate(lst):
    print(i, element)

#Nested for loop for the nested list
nested_list = [[1,2],[4,5],[7,8]]
for i in range(len(nested_list)):
    interior_list = nested_list[i]
    for j in range(len(interior_list)):
        print(interior_list[j])