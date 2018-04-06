import officefurniture


def main():
    desk = officefurniture.OfficeFurniture("brown desk", 5)

    print("material: " + desk.get_material())
    print("length: " + desk.get_length())
    print("height: " + desk.get_height())
    print("width: " + desk.get_width())
    print("Price: " + "${:0,.2f}".format(desk.get_price()))

    print(desk)


main()
