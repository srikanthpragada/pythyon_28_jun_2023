def wish(msg, user):
    print(msg, user)


wish('Hello', 'Joe')
wish("Hi", 'Bill')

wish(user = 'Scott', msg = "Hi")  # keyword args
wish("Hello", user = "James")  #  positional + keyword args
