def div(x,y):
    try:
        result= x/y
    except ZeroDivisionError:
        print('Can not divided by zero')
        return None
    except TypeError:
        print('type not matched')
        return None

    return result

print(div('4','2'))
print(div(4,0))

# unkown exception
def div1(x,y):
    try:
        result= x/y
    except:
        print('Unknown Error')
        return None


    return result

print(div1('4','2'))
print(div1(4,0))

# all exception

def div2(x,y):
    try:
        result= x/y
    except Exception as e:
        print('Unknown Error',e)
        return None


    return result

print(div2('4','2'))
print(div2(4,0))

# else block
# if try block is correct no error is there it will execute the else block

def div3(x,y):
    try:
        result= x/y
    except Exception as e:
        print('Unknown Error',e)
        return None
    else:
        print('nice work')


    return result

print(div3('4','2'))
print(div3(4,0))

# finally block always execute either there is exception or not

def div3(x,y):
    try:
        result= x/y
    except Exception as e:
        print('Unknown Error',e)
        return None
    else:
        print('nice work')
    finally:
        print("finally block clause")
    return result

print(div3('4','2'))
print(div3(4,0))
