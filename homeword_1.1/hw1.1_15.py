while True: #было лень каждый раз заново запускать файл
    user_input = input('Enter your string: ')
    if user_input.isdigit():
        print('Your input includes digits only')
    elif user_input.isalpha():
        print('Your input includes letters only')
    elif user_input.isalnum():
        print('Your input includes digits and letters')
    else:
        print('Error of input')