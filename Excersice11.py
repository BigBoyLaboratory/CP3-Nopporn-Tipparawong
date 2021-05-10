inputNumber = int(input("Put the number to create Pyramid: "))
for i in range(inputNumber):
    inputNumber -= 1
    print(" "*inputNumber, "*"*((i*2)+1))