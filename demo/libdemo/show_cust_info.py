
with open("customers.txt", "rt") as f:
    name = input("Enter customer name :")
    for line in f:
        parts = line.split(",")
        if parts[0].upper() == name.upper():
            print(parts[1], parts[2])
            break
    else:
        print("Sorry! Customer not found!")

