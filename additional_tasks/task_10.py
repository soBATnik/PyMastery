import random


def validate_user_guess(user_answer: int, num_1: int, num_2: int):
    return num_1 + num_2 == user_answer


rand_num_1 = random.randint(1, 10)
rand_num_2 = random.randint(1, 10)

user_num = int(input(f"{rand_num_1} + {rand_num_2} = "))

print("Your answer is correct!" if validate_user_guess(user_num, rand_num_1, rand_num_2) else "You're wrong!")


