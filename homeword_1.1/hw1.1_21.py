word = 'python'
new_list = word.split()
for i in range(len(new_list)):
    
print(id(new_list), ord(new_list)[0])