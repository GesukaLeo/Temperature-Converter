# A program that deals with packages both external and user defined

from math import *
fact = factorial(5)
print("The factorial of number 5! is = :",fact)

#isogram code
def is_isogram(string):
    if type(string) != str:
        raise TypeError('Argument should be a string')
    elif string == " ":
        return (string, False)
    else:
        for i in string:
            if string.count(i) > 1:
                return (string, False)
    return (string, True)


#call the is_isogram function

x= is_isogram("gesuka")
y = is_isogram("posses")
z=is_isogram(12345)
print(x)
print(y)
print(z)