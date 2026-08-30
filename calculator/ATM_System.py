mony = int(input("Enter Your Money: "))
print("Welcome to ATM!")
print("1.deposit\t2.payment\t3.cart b cart\t4.exit")
while True:
    i = int(input("Enter a number: "))
    if i == 1:
        amount = int(input("Enter Amount: "))
        mony += amount
        print("Succesful!")
        print(f"New money: {mony}")
    elif i ==2 :
        amount = int(input("Enter amount: "))
        if mony >= amount:
            mony -= amount
            print("Seccesful!")
            print(f"New money: {mony}")
        else:
            print("No Enough money!")
    elif i == 3 :
        id = int(input("Destination ID: "))
        amount = int(input("Enter amount: "))
        if mony >= amount:
                    mony -= amount
                    print("Seccesful!")
                    print(f"New money: {mony}")
        else:
            print("No Enough money!")
    elif i == 4:
         break
    else:
         print("Wrong input!!")