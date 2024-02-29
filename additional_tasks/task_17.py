

def is_prime(user_num):
    return user_num % 2 != 0 and user_num != 1 or user_num == 2


list_of_primes = [i for i in range(1, 101) if is_prime(i)]

print(list_of_primes)