def increment(n):
    print(id(n))
    n = n + 1
    print(id(n))


def prepend(lst, value):
    lst.insert(0, value)


# v = 100
# print(id(v))
# increment(v)
# print(v)

l = [1, 2, 3]
prepend(l, 100)
print(l)
