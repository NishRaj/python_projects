def pairs_sum_to_target(list1, list2, target):
    indices_list = []
    for idx1, val1 in enumerate(list1):
        for idx2, val2 in enumerate(list2):
            if val1 + val2 == target:
                indices_list.append([idx1, idx2])
    return indices_list
list1 = [1,-2,4,5,9]
list2 = [4,2,-4,-4,0]
print(pairs_sum_to_target(list1, list2, 5))