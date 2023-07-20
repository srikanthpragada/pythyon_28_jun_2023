
class Course:
    # static attribute or class attribute
    taxrate = 18
    # constructor
    def __init__(self, title, duration, fee=5000):
        # object attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate // 100

    def setfee(self, newfee):
        self.fee = newfee


c = Course("AWS", 24, 3500)
print(c.fee)
c.setfee(4000)
print(c.getnetfee())
c2 = Course("Spring", 15)
