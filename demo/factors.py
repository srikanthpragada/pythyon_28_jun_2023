# Print factors of a given number

num = int(input("Enter number :"))
found = False 
for i in range(2, num // 2 + 1):
    if num % i == 0:
        found = True
        print(i, end=' ')

if not found:
    print("No factors found!")
