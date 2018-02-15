years = int(input("Please enter the number of years: "))

month_rainfall = 0

for i in range(1, years + 13):

    for m in range(1, 13):

        rainfall_inch = float(input("Enter the inches of rainfall for this month: "))

        month_rainfall = month_rainfall + rainfall_inch

months = years * 12

print("The number of months is:", months)
print(" The total inches of rainfall is:", month_rainfall)
print(" The average rainfall per month for the entire period is:", format(month_rainfall / months, '.2f'))
