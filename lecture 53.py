def vatCalculate(priceInput):
    result = priceInput + (priceInput * 7 / 100)
    return result

priceInput = int(input("In put price to calculate VAT(THB): "))
print("Net price: ", vatCalculate(priceInput), "THB")