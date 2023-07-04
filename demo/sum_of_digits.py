
num = int(input("Enter number :"))

total = 0
while num > 0:
    digit = num % 10   # rightmost digit
    total += digit
    num = num // 10    # remove rightmost digit

print('Sum of digits = ', total)
