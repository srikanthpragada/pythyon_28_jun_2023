
names = ['Larry Page', 'Bill Gates', 'Peter Norton', 'Joe Stagner']

f = open("names.txt", "wt")

for n in names:
    f.write(n + "\n")

f.close()



