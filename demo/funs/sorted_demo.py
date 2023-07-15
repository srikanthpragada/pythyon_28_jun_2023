nums = [10, 20, -10, -30, 55]

for n in sorted(nums, key = abs):
    print(n, end=' ')
