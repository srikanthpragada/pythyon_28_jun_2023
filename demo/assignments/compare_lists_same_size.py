def compare(lst1, lst2):
    for idx, v1 in enumerate(lst1):
        if v1 != lst2[idx]:
            return idx

    return -1


l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
print(compare(l1, l2))
