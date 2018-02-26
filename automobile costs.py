"""Automobile Costs"""


loan_payment = float(input("Enter a monthly loan payment: $"))

insurance = float(input("Enter a monthly insurance cost: $"))

gas = float(input("Enter a monthly gas cost: $"))

tires = float(input("Enter a monthly tires cost: $"))

maintenance = float(input("Enter a monthly maintenance cost: $"))


def sum_costs(loan_payment,insurance,gas,tires,maintenance):

    total = (loan_payment + insurance + gas + tires + maintenance)

    print("total average per month:")
    print(total)


sum_costs(loan_payment, insurance, gas, tires, maintenance)


def sum_per_year(loan_payment, insurance, gas, tires, maintenance):

    total = (loan_payment + insurance + gas + tires + maintenance) * 12

    print("total costs per year:")
    print(total)


sum_per_year(loan_payment, insurance, gas, tires, maintenance)
