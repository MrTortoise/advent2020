class Slope:
    def __init__(self, data):
        self.rows = data.split('\n')
        self.width = len(self.rows[0])
        self.depth = len(self.rows)

        print(self.width, self.depth)

    def is_tree(self, x, y):
        return self.rows[y][x] == '#'

    def get_number_of_trees(self, distx, disty):
        posx = 0
        posy = 0

        number_of_trees = 0

        while posy < self.depth:
            x = posx % self.width

            if self.is_tree(x, posy):
                number_of_trees = number_of_trees+1

            posx = posx + distx
            posy = posy + disty

        return number_of_trees
