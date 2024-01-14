user_string = input('Input yur string: ')

new_user_string = user_string.strip(" ")    #Без этой строки пробелы перед первым и после последнего слова будут считаться за слова

words_count = new_user_string.count(' ') + 1

print(words_count)

