systemMenu = {"ข้าวหมกไก่":45, "ข้าวมันไก่":40, "ข้าวมันไก่ผสม":50, "ข้าวมันไก่พิเศษ":45}
menuList = []

def sumPrice ():
    sumPrice = 0
    for i in range(len(menuList)):
        sumPrice += int(menuList[i][1])
    print("Total price: ", sumPrice)

def showBill():
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

while True:
    menuName = input("Please enter menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
sumPrice()