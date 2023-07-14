def compare(lst1, lst2):
    if len(lst1) > len(lst2):
        bl = lst1
        sl = lst2
    else:
        bl = lst2
        sl = lst1

    for idx, v1 in enumerate(sl):
        if v1 != bl[idx]:
            return idx

    if len(bl) > len(sl):
        return len(sl)
    else:
        return -1


l1 = [1, 2, 3, 4]
l2 = [1, 2, 4, 4, 5]
print(compare(l1, l2))
