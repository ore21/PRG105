"""Calories by Macronutrient"""

fat_grams = float(input("enter a number of fat grams:"))

carbohydrate_grams = float(input("enter a number of carbohydrate grams:"))

protein_grams = float(input("enter a number of protein grams:"))


def calories_from_fat(fat_grams):
    total = fat_grams * 9
    print("calories from fat is:")
    print(total)


calories_from_fat(fat_grams)


def calories_from_carbs(carbohydrate_grams):
    total = carbohydrate_grams * 4
    print("calories from carbohydrates is:")
    print(total)


calories_from_carbs(carbohydrate_grams)


def calories_from_proteins(protein_grams):
    total = protein_grams * 4
    print("calories from proteins is:")
    print(total)


calories_from_proteins(protein_grams)


def calories_for_day(calories_from_fat, calories_from_carbs, calories_from_proteins):
    total = calories_from_fat + calories_from_carbs + calories_from_proteins
    print("your total calories for the day is:")
    print(total)


calories_for_day(calories_from_fat, calories_from_carbs, calories_from_proteins)








