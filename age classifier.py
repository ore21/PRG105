"""Age Classifier"""

person_age = (int(input("age? ")))

if 0 <= person_age <= 1:
    print("person is an infant")
elif 13 > person_age > 1:
    print("person is a child")
elif 20 > person_age >= 13:
    print("person is a teenager")
elif person_age >= 20:
    print("person is an adult")
