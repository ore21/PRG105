def letter_grade(test_score):
    if test_score >= 90:
        return "A"
    elif 80 >= test_score < 90:
        return "B"
    elif 70 <= test_score < 80:
        return "C"
    elif 60 >= test_score < 70:
        return "D"
    else:
        return "F"


test_score_total = 0
num_tests = 5

for test in range(1, num_tests+1):
    test_score1 = float(input("Enter the numerical test score for test#1: "))
    test_score2 = float(input("Enter the numerical test score for test#2: "))
    test_score3 = float(input("Enter the numerical test score for test#3: "))
    test_score4 = float(input("Enter the numerical test score for test#4: "))
    test_score5 = float(input("Enter the numerical test score for test#5: "))
    test_score_total = test_score1 + test_score2 + test_score3 + test_score4 + test_score5 / 5
    print(" The letter grade is: ")
    print(test_score_total)


def calc_average(test_score_total):

    return test_score_total/5


print("The overall average is:")
print("The overall average letter grade is:")
