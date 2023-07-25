class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Radius = {self.radius}"

    def __eq__(self, other):
        return self.radius == other.radius

    # def __gt__(self, other):
    #     print("__gt__")
    #     return self.radius > other.radius

    def __float__(self):
        return float(self.radius)


c1 = Circle(10)
c2 = Circle(15)
c3 = Circle(5)

lc = [c1, c2, c3]

for c in sorted(lc):
    print(c)


# print(c1)  # str(c1) --> c1.__str__()
# print(c1 == c2)  # c1.__eq__(c2)
# print(c3 > c2)  # c3.__gt__(c2)
# print(c2 < c3)
# print(float(c1) + float(c2))   # c1.__float__()


