import Employee


def main():
    emp = Employee.ProductionWorker('', '', '', '')
    print("Enter information about employee ")
    emp.set_name(input("Enter employee name :"))
    emp.set_number(input("Enter employee number :"))
    emp.set_shift_number(input("Enter employee shift number :"))
    emp.set_pay_rate(input("Enter employee pay rate :"))

    print("Employee information")
    print("Name :", emp.get_name())
    print("number :", emp.get_number())
    print("shift number :", emp.get_shift_number())
    print("Pay rate :", emp.get_pay_rate())


main()
