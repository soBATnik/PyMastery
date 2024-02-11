def counter(user_input):
    count_dict = dict()
    for key in user_input:
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1
    return count_dict

user_input = input("Enter your string, please: ").lower()
result = counter(user_input)
print(result)