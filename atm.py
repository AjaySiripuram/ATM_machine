Username = "Ajay"
Password = "Python123"

Customer_name = input("Enter your name:")
Customer_password = str(input("Enter your password"))

if Customer_name == Username and Customer_password == Password:
    print('''
    1.Deposite
    2.Withdraw
    3.MiniStatement
    4.Exit          
    ''')
    Amount = 50000
    Option = int(input("Select your option:"))

    if Option == 1:
        Dep = int(input("Enter the amount"))
        Amount += Dep
        print("Total amount:",Amount)
    elif Option == 2:
        With = int(input("Enter the amount:"))
        Amount -= With
        print("Total amount:", Amount)
    elif Option == 3:
        print("=======ATM=======")
        print("Username:",Username)
        print("Total amount:",Amount)
        print("Thanks for visiting")
        print("=================")
    elif Option == 4:
        exit()
else:
    print("Please enter correct logins")

