nums = [10, 20, -10, -30, 55]

def sign(v):
    if v > 0:
        return 1
    elif v < 0:
        return -1
    else:
        return 0

# for n in map(abs, nums):
#     print(n)

for n in map(sign, nums):
    print(n)