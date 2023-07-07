
# Lagest digit

num = 75894

largest_digit = 0
while num > 0:
    digit = num % 10
    if digit > largest_digit:
        largest_digit = digit

    num = num // 10

print("Largest digit ", largest_digit)
