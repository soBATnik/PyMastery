def invert(user_dict):
    rev_dict = {value: key for key, value in user_dict.items()}
    return rev_dict


user_dict = {1: 2, 3: 4}
result = invert(user_dict)
print(result)