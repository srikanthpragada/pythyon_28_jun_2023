f = open("names.txt", "rt")

# for name in f.readlines():
#     print(name.strip())

while True:
    line = f.readline()
    if line == "":  # EOF
        break
    print(line, end = '')

f.close()
