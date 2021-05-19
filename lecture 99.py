from tkinter import *
import math

def leftClickButton(event):
    hightPOW2 = math.pow(float((textBoxHight.get()))/100,2)
    weight = float(textBoxWeight.get())
    BMI = weight / hightPOW2
    labelBMI.configure(text=BMI)
    if BMI <= 18:
        labelResult.configure(text="ผอม")
    elif 25 >= BMI >18:
        labelResult.configure(text="หุ่นดี")
    else:
        labelResult.configure(text="อ้วน")

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

labelBMI = Label(MainWindow, text = "BMI")
labelBMI.grid(row=2, column=1)

labelResult = Label(MainWindow, text = "Result")
labelResult.grid(row=3, column=0)

MainWindow.mainloop()