class Mathadd:
    """docstring for ."""

    def __init__(self, x,y):
        self.x=x
        self.y=y
    def sum(self):
        return self.x+self.y

class MathSub(Mathadd):
    """docstring for ."""

    def __init__(self, x,y):
        super().__init__(x,y)

    def substract(self):
        return self.x- self.y

    def sum(self):
        return (self.x+self.y)+10

    def showall(self):
        print('Super',super().sum())
        print('Sub',self.sum())
        return self.x*self.y

Math_obj=MathSub(10,5)
print(Math_obj.showall())
