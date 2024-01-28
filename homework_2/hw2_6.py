user_input_kmph = input("Enter a speed in km/h: ")
user_input_mps = input("Enter a speed in m/s: ")
kmph_to_mps = int(user_input_kmph) * 1000 / 3600
if kmph_to_mps > int(user_input_mps):
    print("Speed in km/h is bigger")
else:
    print("Speed in m/s is bigger")