#create a module  to hold multiples of 2, 3, 4 and 9

#get multiples of Two
def multiples_Of_Two():
    for number in range(1,101):
        if(number%2==0):
            print(number,end=' ')


#get multiples of Three
def multiples_Of_Three():
    for number in range(1,101):
        if(number%3==0):
            print(number,end=' ')


#get multiples of Four
def multiples_Of_Four():
    for number in range(1,101):
        if(number%4==0):
            print(number,end=' ')


#get multiples of Nine
def multiples_Of_Nine():
    for number in range(1,101):
        if(number%9==0):
            print(number,end=' ')