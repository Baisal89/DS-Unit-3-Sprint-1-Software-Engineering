import random

class Product:

    def __init__(self, name = None, price = 10,
        weight = 20, flammability = 0.5,
        identifier = random.randint(1000000, 9999999)):
        self.name = None
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
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
        elif self.weight * self.flammability >=10 < 50:
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

    def __init__(self, name = None, price = 10,
        weight = 10, flammability = 0.5, identifier = None ):
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
