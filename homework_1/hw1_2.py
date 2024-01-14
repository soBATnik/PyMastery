user_string = input('Input yur string: ')

new_user_string = user_string.strip(" ")
words_count = new_user_string.count(' ') + 1

print(words_count)