
def show_max_num(*args: int):
    return max(args)


def main():
    user_first_num = int(input("Enter first num: "))
    user_second_num = int(input("Enter second num: "))
    biggest_value = show_max_num(user_first_num, user_second_num)
    print(f'{biggest_value} is bigger')


main()
