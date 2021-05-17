menuList = []
priceList = []

def sumPrice ():
    sumPrice = 0
    for i in range(len(priceList)):
        sumPrice += int(priceList[i])
    print("Total price: ", sumPrice)

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

while True:
    menuName = input("Please enter menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = (input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
sumPrice()