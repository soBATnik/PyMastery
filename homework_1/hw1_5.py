user_input = input("Enter your phrase with two 'h': ").lower()
new_string = user_input[:user_input.find('h')] + user_input[user_input.rfind('h') + 1:]

print(new_string)
