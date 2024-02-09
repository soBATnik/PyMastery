user_string = 'Andromeda, M 31, NGC 224'

count_letters = list()
count_digits = list()

for i in range(len(user_string)):
    if user_string[i].isalpha():
        count_letters.append(user_string[i])
    elif user_string[i].isdigit():
        count_digits.append(user_string[i])

print('Letters ' + str(len(count_letters)) + ' Digits ' + str(len(count_digits)))