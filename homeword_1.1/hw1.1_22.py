user_string = '''It was early on a fine summer's day, near the end of the eighteenth century, 
when a young man, of genteel appearance,
journeying towards the north-east of Scotland'''
new_string = ' '
for i in range(len(user_string)):
    if i < 36:
        new_string += user_string[i].upper()
    else:
        new_string += user_string[i]

print(new_string)