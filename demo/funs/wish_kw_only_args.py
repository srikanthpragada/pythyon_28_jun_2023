
# Keyword-only args
def wish(*, user="Guest", msg="Hi"):
    print(msg, user)


#wish("Hi", 'Bill')
wish(user="Bill")
