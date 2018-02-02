print("Age Classifier")

person_age = (float(input("age")))

if person_age <= 1 or person_age > 0:
    print("person is an infant")

elif person_age > 1 or person_age < 13:
    print("person is a child")

elif person_age >= 13 or person_age < 20:
    print("person is a teenager")

elif person_age >= 20:
    print("person is an adult")
