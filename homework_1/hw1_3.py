user_input = input('Input your string: ')
half_input = len(user_input) // 2
half_input_1, half_input_2 = user_input[:half_input], user_input[half_input:]
print(half_input_2[1:] + ' ' + half_input_1)
