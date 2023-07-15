def dotask(task, value):
    task(value)


def wish(msg):
    print(msg)


def fun():
    print("Having fun!")


dotask(print, 10)  # passing fun as param
dotask(wish, 'Hello')  # passing fun as param
# dotask(fun, "Hi")  # Error
