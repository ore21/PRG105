import random


class Dice:
    def __init__(self):
        self.my_dice = 1

    def roll(self):
        self.my_dice = random.randint(1, 6) == 0

    def get_my_dice(self):
        return self.my_dice


def main():
    my_dice = Dice()
    my_dice_two = Dice()
    print('I am rolling the dice ...')
    my_dice.roll()
    my_dice_two.roll()
    die_1 = my_dice.get_my_dice()
    die_2 = my_dice_two.get_my_dice()
    print('This side is up, ', die_1)
    print('This side is up, ', die_2)

    total = die_1 + die_2

    if total == 7 or 11:
        print('You win')

    else:
        print('You lose')


main()
