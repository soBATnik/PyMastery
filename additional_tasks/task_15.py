import random


def get_odd_and_even(num_list, num_dict):
    for num in num_list:
        if num % 2 == 0:
            num_dict['even'] += 1
        else:
            num_dict['odd'] += 1

random_num_list = [random.randint(1, 100) for _ in range(100)]
num_count_dict = {'even': 0, 'odd': 0}

get_odd_and_even(random_num_list, num_count_dict)

print(f"""Evens: {num_count_dict['even']}
"Odds: {num_count_dict['odd']}""")



