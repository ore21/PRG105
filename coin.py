import random


class Coin:
    def __init__(self):
        self.side_up = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.side_up = 'Heads'
        else:
            self.side_up = 'Tails'

    def get_side_up(self):
        return self.side_up


def main():
    my_coin = Coin()
    my_coin_two = Coin()
    print('This side is up, ', my_coin.get_side_up())
    print('This side is up, ', my_coin_two.get_side_up())

    print('I am tossing the coins ...')
    my_coin.toss()
    my_coin_two.toss()
    print('This side is up, ', my_coin.get_side_up())
    print('This side is up, ', my_coin_two.get_side_up())


main()
