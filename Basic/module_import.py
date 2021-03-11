import my_math # here mymath is the module also called namspace

print(my_math.sum(2,3))

# import any function

from my_math import substract
print(substract(2,1))

# import all function

from my_math import *
print(substract(2,3))
print(sum(2,3))

#object creation
mmc=MyMath(2,3)

print(mmc.substract())
print(mmc.sum())
