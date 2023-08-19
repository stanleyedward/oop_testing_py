from item import Item

class Keyboard(Item):
    pay_rate = 0.7
    # all = []
    def __init__(self, name: str, price: float, quantity= 0):

        #call to super functio to have access to all atrributes/methods of the parentn class
        super().__init__(
            name, price, quantity
        )