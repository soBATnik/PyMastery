PLACE_A = 20.00
PLACE_B = 15.00
PLACE_C = 10.00

def get_revenue(a_amount, b_amount, c_amount: float) -> float:
    return a_amount * PLACE_A + b_amount * PLACE_B + c_amount * PLACE_C

amount_places_a = float(input("Amount of A-class tickets: "))
amount_places_b = float(input("Amount of B-class tickets: "))
amount_places_c = float(input("Amount of C-class tickets: "))

print(f"Total revenue is {get_revenue(amount_places_a, amount_places_b, amount_places_c)}")
