def find_upper_pos(st):
    for idx, c in enumerate(st):
        if c.isupper():
            return idx

    return -1


print(find_upper_pos('abc'))
print(find_upper_pos('abcDeF'))
