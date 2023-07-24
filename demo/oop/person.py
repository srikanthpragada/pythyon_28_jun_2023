class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email

    def getemail(self):
        return self.__email


p = Person("Bill", "bill@gmail.com")
print(p.__dict__)

print(p._Person__email)

