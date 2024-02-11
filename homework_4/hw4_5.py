def diff(list1, list2):
    diff_list = [i for i in list1 if i not in list2]
    return diff_list

first_list = [1, 2, 3, 4, 5]
second_list = [3, 4, 5, 6, 7]
result = diff(first_list, second_list)
print(result)