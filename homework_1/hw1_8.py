owner = 'daniel'
def greet(name, owner):
    if name == owner:
        print("Hello, boss")
    else:
        print("Hello, guest")

user_input_name = input("Input your name: ").lower()
greet(user_input_name, owner)