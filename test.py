import csv

class Item:
    pay_rate = 0.8 #20% discount
    all = []
    def __init__(self, name: str, price: float, quantity= 0):
        # print(f"I AM CREATED: {name}")
        #Run validations to the reveived arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"
        
        self.name = name 
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)


    def calcluate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price* self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('OOP/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items= list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod   #makes it act liek a isolated function istead of a method
    def is_integer(num):
        #we will count out the floats that are point zero eg 5.0 100.0 etc
        if isinstance(num, float):
            #count out the floats that are point zero 
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
         

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity= 0, broken_phones = 0):
        
        # print(f"I AM CREATED: {name}")
        #Run validations to the reveived arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero"
        # assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"
        

        # self.name = name 
        # self.price = price
        # self.quantity = quantity ----------we use super()----- instead of these

        #call to super functio to have access to all atrributes/methods of the parentn class
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >=0, f"Broken phones {broken_phones} is not greater than or equal to zero"
        self.broken_phones = broken_phones

        # #actions to execute
        # Phone.all.append(self)
        
phone1 = Phone("jscPhonev10", 500, 5, 1)
item1 = Item("laptop", 100, 5)

print(Item.all)
print(Phone.all)


# print(phone1.calcluate_total_price())
# phone2 = Phone("jscPhonev20", 700, 5, 1)
# Item.instantiate_from_csv()
# print(Item.all)
# print(Item.is_integer(7.0))


# item1 = Item("Phone", 100, 5)
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# item2 = Item("Laptop", 1000, 3)
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

# item2.has_numpad = True

# print(Item.__dict__) #all atributes for class lvl
# print(item1.__dict__) #all atributes for uinsstace lvl
# item1 = Item("Phone", 100, 5)
# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)