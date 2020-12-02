from typing import List


class Password:
    def __init__(self, line):
        parts = line.split()
        min_max = parts[0].split('-')

        self.min = int(min_max[0])
        self.max = int(min_max[1])

        self.char = parts[1][0]
        self.password = parts[2]

    @staticmethod
    def get_total_valid(passwords, validator):
        total = sum(1 for p in passwords if validator(p))
        return total
