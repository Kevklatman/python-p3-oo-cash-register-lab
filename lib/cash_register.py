class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.prices = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
            self.prices.append(price)

    def apply_discount(self):
        if self.discount != 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items[-1]
            last_item_quantity = self.items.count(last_item)
            last_item_price = self.prices[-1]
            total_void_amount = last_item_price * last_item_quantity

            self.total -= total_void_amount

            for _ in range(last_item_quantity):
                self.items.pop()
                self.prices.pop()