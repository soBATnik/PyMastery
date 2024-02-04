weekly_income = []
for i in range(0, 7):
    day_income = int(input('Input revenue for a day: '))
    weekly_income.append(day_income)
print(f'Weekly revenue is {sum(weekly_income)}')



# weekly_income = []
#
# day_1 = int(input('Please, input revenue for Monday: '))
# day_2 = int(input('Please, input revenue for Tuesday: '))
# day_3 = int(input('Please, input revenue for Wednesday: '))
# day_4 = int(input('Please, input revenue for Thursday: '))
# day_5 = int(input('Please, input revenue for Friday: '))
# day_6 = int(input('Please, input revenue for Saturday: '))
# day_7 = int(input('Please, input revenue for Sunday: '))
#
# weekly_income.extend([day_1, day_2, day_3, day_4, day_5, day_6, day_7])
#
# weekly_income_total = sum(weekly_income)
# weekly_income_avg = sum(weekly_income) / 7
# print(f'Total weekly revenue is: {weekly_income_total}\n'
#       f'Average revenue per day is: {weekly_income_avg}')