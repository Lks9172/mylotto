# 클래스 선언
class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + " works hard")

    def work(self, job):
        print (self.name +job+ " hard")



person1 = Person("David")
person1.work()
person1.work("develops")