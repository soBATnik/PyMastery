COEF = 0.5


def get_kinetic_energy(mass: float, speed: float) -> float:
    return COEF * mass * speed ** 2


user_mass = float(input("Enter your mass: "))
user_speed = float(input("Enter your speed: "))
print(f"Your energy is {get_kinetic_energy(user_mass, user_speed)}")