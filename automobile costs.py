def ask_for_expenses():
    monthly_loan_payment = float(input(" how much do you pay for your loan every month:"))

    monthly_insurance_payment = float(input("how much do you pay for your insurance every month:"))

    monthly_gas_payment = float(input("how much do you pay for your gas every month"))

    monthly_oil_payment = float(input("how much do you pay for your oil every month:"))

    monthly_tire_payment = float(input("how much do you pay for your tire every month:"))

    monthly_maintenance_payment = float(input("how much do you pay for you maintenance every month:"))

    return monthly_loan_payment, monthly_insurance_payment, monthly_gas_payment, monthly_oil_payment, monthly_tire_payment, monthly_maintenance_payment


def calculate_total_monthly_cost(payment1, payment2, payment3, payment4, payment5, payment6):
    total_monthly_cost = payment1 + payment2 + payment3 + payment4 + payment5 + payment6
    return total_monthly_cost


def calculate_total_annual_cost(total_monthly_cost):
    total_annual_cost = total_monthly_cost * 12
    return total_annual_cost


def print_details(total_monthly_cost, total_annual_cost):
    print()
    print("your total monthly cost is $" + format(total_monthly_cost, ",.2f" +
                                                  "\nyour total annual cost is $" + format(total_annual_cost, ",.2f")))


def main():
    loan_payment, insurance_payment, gas_payment, oil_payment, tire_payment, maintenance_payment = ask_for_expenses()

    total_monthly_cost = calculate_total_monthly_cost(loan_payment, insurance_payment, gas_payment,
                                                      oil_payment, tire_payment, maintenance_payment)

    total_annual_cost = calculate_total_annual_cost(total_monthly_cost)
    print_details(total_monthly_cost, total_annual_cost)


main()


