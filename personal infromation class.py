""""personal information class"""


class PersonalInfo:
    def __init__(self, names, addresses, ages, numbers):
        self.__names = names
        self.__addresses = addresses
        self.__ages = ages
        self.__numbers = numbers

    def set_names(self, name):
        self.__names = name

    def set_addresses(self, address):
        self.__addresses = address

    def set_ages(self, age):
        self.__ages = age

    def set_numbers(self, number):
        self.__numbers = number

    def get_names(self):
        return self.__names

    def get_addresses(self):
        return self.__addresses

    def get_ages(self):
        return self.__ages

    def get_numbers(self):
        return self.__numbers


def main():
    person1 = PersonalInfo("Ben", "123 6th St. Melbourne, FL 32904", 18, "800 - 576 - 5677")
    person2 = PersonalInfo("Bill", "71 Pilgrim Avenue Chevy Chase, MD 20815", 20, "745 - 600 - 3454")
    person3 = PersonalInfo("Jack", "70 Bowman St. South Windsor, CT 06074", 25, "800 - 678 - 4492")

    print("Name: " + str(person1.get_names() + "\n Address: " + person1.get_addresses() + "\n Age: " + str(person1.get_ages())
          + "\n Phone Number: " + str(person1.get_numbers())))
    print("Name: " + str(person2.get_names() + "\n Address: " + person2.get_addresses() + "\n Age: " + str(person2.get_ages())
          + "\n Phone Number: " + str(person2.get_numbers())))
    print("Name: " + str(person3.get_names() + "\n Address: " + person3.get_addresses() + "\n Age: " + str(person3.get_ages())
          + "\n Phone Number: " + str(person3.get_numbers())))


main()
