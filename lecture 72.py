menuList = []

def sumPrice ():
    sumPrice = 0
    for i in range(len(menuList)):
        sumPrice += int(menuList[i][1])
    print("Total price: ", sumPrice)

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number])

while True:
    menuName = input("Please enter menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append([menuName, menuPrice])

showBill()
sumPrice()