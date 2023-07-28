

try:
    v = int(input("Enter number :"))
    print(100 // v)
except ValueError as ex:
    print("Sorry! ", ex)
except ZeroDivisionError:
    print("Sorry! Zero is not valid")

print("The End")



