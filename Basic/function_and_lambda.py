def welcome():
    print('Welcome you')
    for x in range(10):
        print(x+1, end=',')

def namFunc(name):
    print(f'Welcome Mr.{name}')



# positional argument

def person_details(name,age, country):
    print(name,age,country)

person_details('abul',24,'AUS')
#keyword argument
person_details(country='Canada', name='Billings', age=23)

#defualt value
def person_details1(name,age,country='Bangladesh'):
    print(f'Name:{name}')
    print(f'Age:{age}')
    print(f'Country{country}')

person_details1(name='abul',age=23)
person_details1(name='Peter',age=43, country='US')
person_details1('Kashem',44)

# arbitary argument

def arbitary_arg(*students):
    print(students)

arbitary_arg('anuz','sajal','nayan','khayer','rahman')



def arb_pos(captain, *name):
    print(captain)
    print(name)

arb_pos('hammad','mahmud','kabir','peter','hanan')


def arg_dict(captain, **students):
    print(captain)
    print(students)

arg_dict(captain='anuz', st1='kashem', st2='halim', st3='rahman', st4='kuddus')


# lambda
