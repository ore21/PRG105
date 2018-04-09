""""Inheritance"""


class OfficeFurniture():

    def __init__(self, material, length, width, height, price):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_item_price(self):
        return self.__price + self.__length

    def __str__(self):
        item = self.__material + " length " + str(self.__length) + " width " + str(self.__width) + " height " + \
               str(self.__height) + " price: " + str(self.__price) + " total:"
        return item


# desk = OfficeFurniture("brown", 1, 10)
#

class Desk(OfficeFurniture):

    def __init__(self, material, length, width, height, price, location):
        OfficeFurniture.__init__(self, material, length, height, width, price)

        self.__location = location

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def __str__(self):
        line = "material: " + self.get_material() + "location: " + self.get_location() + " length " \
                    + str(self.get_length()) + " Each: ${:0,.2f}".format(self.get_price()) \
                    + "total: ${:0,.2f}".format(self.get_item_price())
        return line

