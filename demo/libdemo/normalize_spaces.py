import re

with open("test.txt", "rt") as f:
    contents = f.read()

newcontents = re.sub(r" +", ' ', contents)
newcontents = re.sub(r"\n+", '\n', newcontents)

print(newcontents)

# with open("test.txt", "wt") as f:
#      f.write(newcontents)
