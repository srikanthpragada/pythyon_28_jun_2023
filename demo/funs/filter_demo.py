nums = [10, 20, -10, -30, 55]

def ispositive(n):
    return n > 0


for n in filter(ispositive, nums):
    print(n)

for c in filter(str.isupper,  "AbcDef"):
    print(c)
