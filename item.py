import csv

class Item:
    pay_rate = 0.8 #20% discount
    all = []
    def __init__(self, name: str, price: float, quantity= 0):
        # print(f"I AM CREATED: {name}")
        #Run validations to the reveived arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero"
        
        self.__name = name #_ makes it legal for it no assign name even with the property decorator name()method
        self.__price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price* self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    #property decorator = read-only attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("the name is too long")
        else:
            self.__name = value 

    def calcluate_total_price(self):
        return self.__price * self.quantity

    
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
        
    # @property
    # def read_only_name(self):
    #     return 'AAA'


         

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    def __connect(self,smpt_server): #__ makes it private ie can only be accessed inside the claass
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, StnaleyedaWrd
        """
    def __send(self):
        pass


    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()