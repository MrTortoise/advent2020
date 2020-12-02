class Password:
    def __init__(self, line):
        parts = line.split()
        min_max = parts[0].split('-')

        self.min = int(min_max[0])
        self.max = int(min_max[1])

        self.char = parts[1][0]
        self.password = parts[2]

    def is_valid(self):
        total = sum(1 for c in self.password if c == self.char)
        return self.min <= total <= self.max

