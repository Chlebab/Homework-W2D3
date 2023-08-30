class Pub:
    def __init__ (self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, customer, drink, amount, alcohol_level):
        if customer.age > 18 and customer.drunkness < 3:
            self.till += amount
            customer.buy_drink(drink, amount)
            customer.drunkness += alcohol_level
        else:
            pass

    def sell_food(self, customer, name, price, rej_level):
        self.till += price
        customer.buy_food(name, price)
        customer.drunkness -= rej_level

