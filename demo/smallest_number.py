
a, b, c = 10, 15, 5

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
elif b < c:
    print(b)
else:
    print(c)


smallest = a
if b < smallest :
    smallest = b

if c < smallest:
    smallest = c

print(smallest)
