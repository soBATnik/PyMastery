user_input = input("Enter a sum: ")
fed_tax = int(user_input) * 0.05
reg_tax = int(user_input) * 0.025
gen_tax = fed_tax + reg_tax
gen_sum = int(user_input) * 1.075

print(f'''Federal tax: {fed_tax}
Regional tax: {reg_tax}
Total taxes: {gen_tax}
Total sum is {gen_sum}
''')
