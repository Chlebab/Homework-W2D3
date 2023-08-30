class Customer:
    def __init__ (self, name, wallet, age, drunkness):
        self.name = name
        self.wallet = wallet
        self.age = age    
        self.drunkness = drunkness   
        
    
    def buy_drink(self, drink, amount):
        self.drink = drink
        self.wallet -= amount

    def buy_food(self, name, amount):
        self.name = name
        self.wallet -= amount

