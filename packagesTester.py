from math import *
import re

#check if its Not a Number NaN
test = float('nan')
x=isnan(test)
print("The boolean result is :",test)
print("The ultimate result is now :",x)


#check for otherwise
test2 = float(3456)
y=isnan(test2)
print(test2)
print(y)

#dictionaries methods

shopping_List = {
    "Eggs":20.00,
    "Bread":50.00,
    "Blue Band":250.25,
    "Juice Mango": 80.40,
    "Apple":40.24,
    "tissue":100,
    "mango":30.50
}

#print our items in the dictionary
print(shopping_List)

#values only
print(shopping_List.values())

#Keys only
print(shopping_List.keys())

#iterate on the dictionary
for i in shopping_List:
    print("%s  %.2f" %(i, shopping_List[i]))

#compute the total of values in the dictionary
Total =0
for item in shopping_List:
    Total += shopping_List[item]
print("Total=",Total)

#Pig latin translator program

original ="Gesuka"
pgy = "ay"
pgy2 = "way"

word = original.lower()

#check for starting letter using regular expressions
first = word[0]
if (first == "a" or "e" or "i" or "o" or "u"):
    newword = word + pgy2
    print(newword)
else:
    newword = word + first + pgy
    print(newword[1:])
    
