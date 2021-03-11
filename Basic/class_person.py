class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age
    def change_name(self,name):
        self.name=name

    def details(self):
        print(self.name, self.age)
obj1=Person('Billings',35)
obj1.details()

# direct modification

person_x=Person(name='Stone Cold', age=49)
person_x.details()

person_x.change_name('Rock')

person_x.details()
