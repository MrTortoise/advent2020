from day3.slope import Slope


def day31():
    data = open("data.txt").read()
    slope = Slope(data)
    print(slope.get_number_of_trees(3,1))


if __name__ == '__main__':
    day31()
