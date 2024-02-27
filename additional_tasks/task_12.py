COEF = 0.5
G = 9.81


def get_falling_distance(time_to_fall: int) -> float:
    return COEF * G * time_to_fall ** 2


i = 1
while i != 11:
    print(f"{i} - {get_falling_distance(i):.2f}")
    i += 1
