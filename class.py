class Item:

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 500
item1.quanity = 1
item1.calculate_total_price()
