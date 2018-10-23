print("Welcome to Sanjiv's Point of Sale Fruit Stand.\n")
Shopping_Cart=[]
reg=0
print(" 1. Add item,\n 2. Remove item,\n 3. View Cart,\n 0. Exit\n")

option=int(input("Enter an option:  "))
while option != 0:
    if option == 1:
        
        Products={"Lemon":10, "Grape":200, "Apple":300}
        for item in Products:
            print(item,":", Products[item])

        item=input("\nEnter the item:  ")
        qnty=int(input("Enter the quantity:  "))
        Shopping_Cart.append(item)
        print(Shopping_Cart)
        
        if item == 'Lemon':
            x=(Products["Lemon"])
            

        elif item == 'Grape':
            x=(Products["Grape"])
            

        elif item == 'Apple':
            x=(Products["Apple"])
           

        def S(x,qnty):
            return x*qnty
            return x,qnty,S,reg, Sub_Total
        Sub_Total=S(x,qnty)

        reg += Sub_Total
        print("THE SUB-TOTAL IS:  ",reg)
        
    elif option == 2:
        if Shopping_Cart==[]:
            print("Add a Product First")
            option=int(input("Enter an option:  "))
        else:
            item=input("\nEnter the item:  ")
            Shopping_Cart.remove(item)
            Tot=reg-Sub_Total
            print("The Total is:  KES",Tot)
            exit();
        
        

    elif option == 3:
        print(Shopping_Cart)
        

    elif option != 0:
        print("You did not enter a valid number")
    option=int(input("Enter an option:  "))

   

else:
    print("Shopping Cart program closed")

print("Total is:  ", reg)
