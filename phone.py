from item import Item

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