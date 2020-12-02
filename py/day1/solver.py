class Solver(object):

    def solve2(self, values):
        length = len(values)
        for x in range(length):
            for y in range(1, length):
                first = values[x]
                second = values[y]
                if first + second == 2020:
                    return first * second
        raise Exception("did not find match")

    def solve3(self, values):
        length = len(values)
        for x in range(length-2):
            for y in range(1, length-1):
                for z in range(2, length - 1):
                    first = values[x]
                    second = values[y]
                    third = values[z]
                    if first + second + third == 2020:
                        return first * second * third
        raise Exception("did not find match")


