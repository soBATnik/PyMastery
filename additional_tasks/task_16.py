

def is_prime(user_num: int):
    return "Your number is prime" if user_num % 2 != 0 and user_num != 1 or user_num == 2 else "Your number is not prime"


user_number = int(input("Enter your number: "))
print(f'{is_prime(user_number)}')