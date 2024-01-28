user_input = input("Enter amount of seconds: ")
day = int(user_input) // 86400
hour = int(user_input) % 86400 // 3600
min = int(user_input) % 86400 % 3600 // 60
sec = int(user_input) - day * 86400 - hour * 3600 - min * 60
print(f'''<{day}:{hour}:{min}:{sec}>
''')