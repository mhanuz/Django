class Math:
    """docstring for ."""

    def __init__(self, x,y):
        self.x=x
        self.y=y
    def sum(self):
        return self.x+self.y

class MathExtend(Math):
    """docstring for ."""

    def __init__(self, x,y):
        super().__init__(x,y)
        self.x=x
        self.y=y

    def substract(self):
        return self.x- self.y

MathExtend_obj=MathExtend(10,2)
print(MathExtend_obj.substract())
print(MathExtend_obj.sum())
