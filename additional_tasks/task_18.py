PERCENTAGE = 0.05


def calculate_deposit(amount: float, period: int) -> float:
    return amount + amount * PERCENTAGE * period

user_amount_of_money = float(input("Enter amount of money: "))
user_period = int(input("Enter amount of months: "))
print({calculate_deposit(user_amount_of_money, user_period)})