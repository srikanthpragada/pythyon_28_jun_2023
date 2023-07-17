nums = [10, 20, -11, -30, 55]

for n in filter(lambda v: v > 0, nums):
    print(n)

for n in filter(lambda v: v % 2 == 0, nums):
    print(n)
