import random
lottery_numbers = []
for i in range(0, 7):
    lottery_number = [random.randint(0, 10) for i in range(0, 7)]
    int_lottery_number = int(''.join(map(str, lottery_number)))
    lottery_numbers.append(int_lottery_number)
print(lottery_numbers)








# import random
# lottery_numbers = []
#
# for i in range(0, 7):
#     lottery_number = []
#     for numb in range(0, 7):
#         lottery_number.append(random.randint(0, 10))
#     int_lottery_number = int(''.join(map(str, lottery_number)))
#     lottery_numbers.append(int_lottery_number)
#
# print(lottery_numbers)
