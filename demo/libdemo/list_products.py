f = open("products.txt", "rt")
ef = open("errors.txt", "wt")

products = []
for line in f:
    parts = line.split(",")
    if len(parts) < 2:
        ef.write(line)
        continue
    try:
        name = parts[0]
        price = int(parts[1].strip())
        products.append((name, price))
    except:
        ef.write(line)

f.close()
ef.close()

for name, price in sorted(products, key=lambda t: t[1]):
    print(f"{name:30} {price:8}")
