from tkinter import *
import math

def leftClickButton(event):
    hightPOW2 = math.pow(float((textBoxHight.get()))/100,2)
    weight = float(textBoxWeight.get())
    BMI = weight / hightPOW2
    labelBMI.configure(text=BMI)
    if  18.5 > BMI:
        labelResult1.configure(text="ผอมเกินไป")
    elif 18.5 <= BMI <= 22.9 :
        labelResult1.configure(text="น้ำหนักปกติ เหมาะสม")
    elif 22.9 < BMI <= 24.9:
        labelResult1.configure(text="น้ำหนักเกิน")
    elif 24.9 < BMI <= 29.9 :
        labelResult1.configure(text="อ้วน")
    else:
        labelResult1.configure(text="อ้วนมาก")

MainWindow = Tk()

labelHight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHight.grid(row=0, column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0, column=1)

labelWeight = Label(MainWindow, text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(MainWindow, text = "คำนวณ BMI")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2, column=0)

labelBMI = Label(MainWindow, text = "")
labelBMI.grid(row=2, column=1)

labelResult = Label(MainWindow, text = "ผลลัพธ์")
labelResult.grid(row=3, column=0)

labelResult1 = Label(MainWindow, text = "")
labelResult1.grid(row=3, column=1)

MainWindow.mainloop()