st = "10,30,40,pq,50,ab,20"

total = 0
for n in st.split(","):
    if n.isdigit():
        total += int(n)

print(total)
