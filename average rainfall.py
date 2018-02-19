years = int(input("Please enter the number of years: "))
grand_total = 0
for year in range(0, years):
    year_total = 0
    print("Year " + str(year + 1))
    for months in ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec "):
        rainfall_inch = float(input("Enter the inches of rainfall for " + months + ": "))
        year_total += rainfall_inch
        grand_total += rainfall_inch
    print("average rainfall per month is: ", format(year_total / 12))


print(" The total inches of rainfall is:", grand_total)
print(" The average rainfall per month for the entire period is:", format(grand_total / (years * 12), ".2f"))
