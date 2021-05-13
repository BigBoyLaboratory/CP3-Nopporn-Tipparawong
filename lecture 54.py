def login():
    userNameInput = input("Username: ")
    passwordInput = input("Password: ")
    if userNameInput == "admin" and passwordInput == "1234":
        print("Login success")
    else:
        print("Usermane or password incorrect")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input("select menu: "))
    if userSelected == 1:
        price = int(input("price of product: "))
        print("price + 7%vat : ", vatCalculator(price), "THB")
    elif userSelected == 2:
        print("Total price + 7%vat : ", priceCalculator())
    else:
        print("No selected menu")
        menuSelect()

def vatCalculator(price):
    vat = 7
    result = price + (price * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
showMenu()
menuSelect()