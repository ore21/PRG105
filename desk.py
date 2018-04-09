import OfficeFurniture


def main():
    desk = OfficeFurniture.OfficeFurniture("Walnut", "60 Inches", "24 Inches", "30 inches", "$ 675.00")
    print("Desk")
    print("material: " + desk.get_material())
    print("length: " + desk.get_length())
    print("height: " + desk.get_height())
    print("width: " + desk.get_width())
    print("Price: " + desk.get_price())
    print(desk)


main()
