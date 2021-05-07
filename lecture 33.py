#price = 100
#vat = 7
#result = 100+(100*7/100)
#print (result)

price = int(input("ใส่ราคาสินค้าที่คุณซื้อ: "))
vat = 7
result = price+(price*vat/100)
print ("ราคาสินค้ารวม vat: = ", result, "บาท")