import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div (a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b <= 0 or a < 0 or a == 1:
        raise ValueError
    if b == math.e:
        return math.log(a)
    return math.log(a, b)

def exp(a, b):
    return a**b




def add(a, b):
    pass
import math

def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def logarithm(a,b):

    if b<=0 or a<0 or a==1:
        raise ValueError
    if b==math.e:
        return math.log(a)
    return math.log(a,b)

def exponent(a,b):
    return a**b