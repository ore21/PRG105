"""pennies for pay"""

numberOfDaysWorked = int(input("please enter how mny days you worked: "))
totalNumberOfPennies = 0

print()

print("Day \tSalary\n----\t-------")
for currentDay in range(numberOfDaysWorked):
    penniesForTheDay = 2 ** currentDay
    totalNumberOfPennies += penniesForTheDay
    print(currentDay + 1, "\t",  penniesForTheDay)

totalPay = totalNumberOfPennies * 0.01

print("\nTotal pay: $", totalPay, sep="")
