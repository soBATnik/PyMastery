time_list = [10, 15, 20, 25, 30]
kcal_per_min = 4.2
kcal_per_time = []

for i in time_list:
    kcal_per_time.append(i * kcal_per_min)
    print(f'{i}min - {kcal_per_min} kcal')