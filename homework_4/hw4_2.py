def average(stud_dict):
    average_score = sum(stud_dict.values())/len(stud_dict)
    list_of_the_best = [key for key, value in stud_dict.items() if value > average_score]
    return list_of_the_best

students = {'John Smith': 80, 'Meryl Strip': 90}
print(average(students))