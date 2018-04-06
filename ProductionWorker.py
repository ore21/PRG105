import Employee


def main():
    print("Enter information about employee :")
    name = input("Enter employee name :")
    number = input("Enter employee number :")
    shift = input("Enter employee shift number :")
    pay = input("Enter employee pay rate :")

    Employee(name, number, shift, pay)


emp = ("")

print("Employee information :")
print("Name :", emp.get_name())
print("number :", emp.get_number())
print("shift number :", emp.get_shift_number())
print("Pay rate :", emp.get_pay_rate())

main()
