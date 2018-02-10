"""average Rainfall"""
totalNumberOfMonths = 0
totalNumberOfRainfall = 0
userNumberOfYears = int(input(" please enter the number of years: "))

for currentYear in range(1, userNumberOfYears + 1):
    for currentMonth in range(1, 13):
        monthlyRainfallInches = float(input(" please type the inches of " +\
                                            "rainfall per month " + format(currentMonth, "d") +\
                                             ", year" + format( currentYear, "d") + ":"))
        totalNumberOfRainfall += monthlyRainfallInches
        totalNumberOfMonths += 1

averageRainfall = totalInchesOfRainfall / totalNumberOfMonths

print()

print("number of months:" + format(totalNumberOfMonths, "d"), "total" + \
      "inches of rainfall:" + format(totalNumberOfRainfall, ".2f"), \
      "average rainfall:" + format(averageRainfall, ".2f", sep="\n"))




