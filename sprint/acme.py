from random import randint


class Product(object):
    def __init__(self, name, price=10, weight=20, flammability=.5,
                 identifier=randint(1000000, 9999999)):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < .5:
            return 'Not so stealable...'
        elif ratio < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            return '...fizzle.'
        elif product < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

    def __str__(self):
        return ('%s\nPrice: %s\nWeight: %s\nFlammability: %s\nIdentifier: %s' %
                (self.name, self.price, self.weight,
                 self.flammability, self.identifier))


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=.5):
        Product.__init__(self, name, price, weight, flammability)
        self.weight = int(10)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
