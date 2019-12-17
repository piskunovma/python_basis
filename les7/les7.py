class Sq:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.sq = x * y

    def __add__(self, other):
        return Sq(self.x + other.x, self.y + other.y)


a = Sq(2, 4)
b = Sq(4, 6)
c = a + b
print(1)