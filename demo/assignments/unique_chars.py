
names = ['java', 'javascript', 'typescript', 'python', 'c']

chars = set()
for n in names:
    chars = chars | set(n)

print(chars)
