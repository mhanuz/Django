# class variable and instanace variable and their working approch

class Alien:
    """docstring for ."""
    legs=5 # class variable

    def __init__(self, name):
        self.name = name # instance variable

# instanace object or instantiations
alien1=Alien('Wovem')
alien2=Alien('Shuivom')

print(alien1.name)
print(alien2.name)

# change the value of class variable
# Class name and the variable
Alien.legs=10

print(alien1.legs)
print(alien2.legs)
# change the class variable only for an object

alien1.legs=90
print(alien1.legs)
print(alien2.legs)


# change the value of class variable through any object

alien1.__class__.legs=90
print(alien1.legs)
print(alien2.legs)
