print ("Welcome to Fruit-Shop,", "Please login")
usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "BigBoy" and passwordInput == "0808":
    print ("Login Success")
    print ("Select Product Below")
    print ("====================")
    print ("1.Apple  =  20 THB")
    print ("2.Banana =  30 THB")
    print ("3.Orange =  25 THB")
    print ("====================")
    userSelected = int(input(">>>"))
    if userSelected == 1:
        price = 20
        numberProduct = int(input("Number of Product You Want to Buy: "))
        Total = price * numberProduct
        print (Total, "THB")
    elif userSelected == 2:
        price = 30
        numberProduct = int(input("Number of Product You Want to Buy: "))
        Total = price * numberProduct
        print (Total, "THB")
    elif userSelected == 3:
        price = 25
        numberProduct = int(input("Number of Product You Want to Buy: "))
        Total = price * numberProduct
        print (Total, "THB")
    else:
        print ("No Product")

else:
    print ("Username or Password Incorrect, Please try again.")