user_input = input("Enter your string: ")

new_string = ""
for i in range(len(user_input)):
    if i % 3:
        new_string = new_string + user_input[i]
print(new_string)

