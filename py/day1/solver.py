class Solver(object):

    def solve(self, values):
        length = len(values)
        for x in range(length):
            for y in range(1, length):
                first = values[x]
                second = values[y]
                if first + second == 2020:
                    return first * second
        raise Exception("did not find match")


