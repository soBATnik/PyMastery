FED_TAX = 0.05
MUN_TAX = 0.025


def calculate_fed_taxes(income: float) -> float:
    return income * FED_TAX


def calculate_mun_taxes(income: float) -> float:
    return income * MUN_TAX


cash_income = float(input("Enter monthly revenue: "))

print(f"""Federal tax: ${calculate_fed_taxes(cash_income)}
Municipal tax: ${calculate_mun_taxes(cash_income)}
Total amount of monthly taxes is ${calculate_fed_taxes(cash_income) + calculate_mun_taxes(cash_income)}""")