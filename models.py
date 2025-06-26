

class Pizza:
    name = ""
    ingredients = ""
    price = 0.0
    vegetarian = False

    def __init__(self, name, ingredients, price, vegetarian):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.vegetarian = vegetarian
