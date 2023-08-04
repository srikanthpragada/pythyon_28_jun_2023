import re

with open("old_man.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

for w in sorted(set(words)):
    print(f"{w:20} {words.count(w):3}")

