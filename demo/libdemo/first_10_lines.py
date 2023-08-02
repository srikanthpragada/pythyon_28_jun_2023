filename = input("Enter filename :")
try:
    f = open(filename, "rt")
    count = 1
    for line in f:
        print(line, end='')
        count += 1
        if count > 10:
            break

    f.close()
except Exception as ex:
    print("Error :" + ex)
