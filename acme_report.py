import random
from acme import Product


class Product:

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = None
        self.price = 10
        self.weight = 20
        self.flammability = 0.5from random import randint, sample, uniform


adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


class Report(Product):

    def __init__(self, num_products=None, products_set=None):
        super().__init__()
        self.num_products = num_products
        self.products = products
        self.products_set = products_set

    def generate_products(self, num_products=30):

        # TODO - your code! Generate and add random products.
        sefl.products = [" ".join(sample(adjectives, 1) + sample(nouns, 1))
                         for p in range(num_products)]
        sefl.products_set = set(self.products)
        self.products = len(self.products_set)

        print("Unique product names:", self.products)
        return products


def inventory_report(self, products):

        avarage_price = self.price/products
        print("Avarage price", avarage_price)

        avarage_weight = self.weight/products
        print("Avarage weight", avarage_weight)

        avarage_flammability = self.flammability/products
        print("Avarage flammability", avarage_flammability)

        return

pass  # TODO - your code! Loop over the products to calculate the report.
if __name__ == '__main__':
        inventory_report(generate_products())

        self.identifier = identifier


def stealability(self):

        """ Outputs the product's stealability """

        if self.weight / self.price < 0.5:
            print("'No so stealable'")
            return
        elif self.weight / self.price >= 0.5 < 1.0:
            print("'Kinda stealable'")
            return
        else:
            print("'Very stealable!'")


def explode(self):
        """ Prints the outcome of the flammability"""

        if self.weight * slef.flammability < 10:
            print("'...fizzle'")
            return
        elif self.weight * self.flammability >= 10 < 50:
            print("'...boom'")
            return
        else:
            print("'....BABOOM!!'")
            return
        pass


class BoxingGlove(Product):
    """
    BoxingGlove subclass of Product
    """

    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=None):
        super().__init__(weight)

    def explode(self):
        """ Prints the outcome of the flammability"""
        print("""...it's a glove""")

    def punch(self):
        """ Prints the reaction after boxing gloves hits the enemy """
        if self.weight < 5:
            print("'That tickles.'")
            return
        elif self.weight >= 5 < 15:
            print("'Hey that hurts!'")
            return
        else:
            print("Ouch!!")
            return

    pass
