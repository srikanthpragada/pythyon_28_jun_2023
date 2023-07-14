
# Positional-only args
def wish(user="Guest", msg="Hi", /):
    print(msg, user)


wish('Bill')
#wish(user="Bill")
