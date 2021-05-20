class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to ", self.name, self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Nopporn"
customer1.lastname = "T"
customer1.addCart()

customer2 = Customer()
customer2.name = "Orasi"
customer2.lastname = "S"
customer2.addCart()

customer3 = Customer()
customer3.name = "Noppargone"
customer3.lastname = "T"
customer3.addCart()

customer4 = Customer()
customer4.name = "Aungsuweporn"
customer4.lastname = "T"
customer4.addCart()