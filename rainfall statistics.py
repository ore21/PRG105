"""rainfall statistics"""


def main():

    total = 0

    monthly_list = []

    for i in range(12):

        rainfall = float(input("Enter the amount of rainfall for this month :"))

        monthly_list.append(rainfall)

        total += rainfall

    print(monthly_list)

    print("The total amount of rainfall in the year is :", total)

    print("The average amount of rainfall for every month in the year is :",

          total / 12)

    print("The month with the highest amount of rainfall is :", max(monthly_list))

    print("The month with the lowest amount of rainfall is :", min(monthly_list))


main()
