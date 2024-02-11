def to_dict(func_list):
    new_dict = {num: num for num in func_list}
    return new_dict

num_list = [1, 2, 3, 4]
new_dict = to_dict(num_list)
print(new_dict)