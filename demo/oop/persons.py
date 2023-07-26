class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

    def setemail(self, newemail):
        self.email = newemail


class Employee(Person):
    def __init__(self, name, email, job, company):
        super().__init__(name, email)
        self.job = job
        self.company = company

    def __str__(self):
        return super().__str__() + f" - {self.job} - {self.company}"

    def change(self, *, job=None, company=None):
        if job is not None:
            self.job = job

        if company is not None:
            self.company = company


e = Employee("David", "david@gmail.com", "Programmer", "Google")
e.setemail("david@google.com")
e.change(job="Sr. Programmer")
print(e)  # e.__str__()
