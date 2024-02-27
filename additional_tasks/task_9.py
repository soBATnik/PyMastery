FT_TO_INCHES = 12


def convert_ft_to_inch(measure: float) -> float:
    return measure * FT_TO_INCHES


user_ft = float(input(f"Enter ft: "))
print(f"{user_ft}ft is {convert_ft_to_inch(user_ft)}in")