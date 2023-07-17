data = ['A123X5', 'DE1Y5', 'DEF9', 'PQ123', 'AB']


def extract_number(s):
    st = ""
    for c in s:
        if c.isdigit():
            st += c

    return int(st) if len(st) > 0 else 0


# for n in map(extract_number, data):
#     print(n)

print(sum(map(extract_number, data)))