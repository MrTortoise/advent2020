from day3.slope import Slope


def day31():
    data = open("data.txt").read()
    slope = Slope(data)
    print(slope.get_number_of_trees(3, 1))


def day32():
    data = open("data.txt").read()
    slope = Slope(data)
    res = slope.get_number_of_trees(1, 1) * slope.get_number_of_trees(3, 1) * slope.get_number_of_trees(5,
                                                                                                        1) * slope.get_number_of_trees(
        7, 1) * slope.get_number_of_trees(1, 2)
    print(res)


if __name__ == '__main__':
    day32()
