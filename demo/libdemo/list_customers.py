import re

f = open("cust.txt", "rt")
customers = {}

for line in f.readlines():
    # look for name
    m = re.search("[A-Za-z ]+", line)
    if m is None:
        continue

    name = m.group(0).strip()
    if len(name) == 0:
        continue

    # Look for mobile
    m = re.search("[0-9]+", line)
    if m is None:
        continue

    mobile = m.group(0)

    customers[name] = mobile


for name, mobile in sorted(customers.items()):
    print(f"{name:20}  {mobile}")




