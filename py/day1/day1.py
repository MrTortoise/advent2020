from day1.solver import Solver


def day11():
    data = open("data.txt")
    lines = data.read().split()
    int_lines = [int(i) for i in lines]
    solver = Solver()
    result = solver.solve2(int_lines)
    print(result)


def day12():
    data = open("data.txt")
    lines = data.read().split()
    int_lines = [int(i) for i in lines]
    solver = Solver()
    result = solver.solve3(int_lines)
    print(result)


if __name__ == '__main__':
    day12()
