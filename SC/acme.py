import random

class Product():
    '''For creating products to be inventoried.'''
    def __init__(
            self, 
            name, 
            price = 10, 
            weight = 20, 
            flammability = 0.5, 
            identifier = random.randint(1000000, 10000000),
            ):
        self.name = name # Name of product
        self.price = price # Price of product
        self.weight = weight # Weight of product
        self.flammability = flammability # Flammability of product
        self.identifier = identifier # Identification code for product
        
    def stealability(self): # Stealability = price / weight
        steal_factor = self.price / self.weight
        if steal_factor >= .05 and steal_factor < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'
    
    def explode(self): # Explode = flammability * weight
        flamm_index = self.flammability * self.weight
        if flamm_index < 10:
            return '...fizzle.'
        elif flamm_index >=10 and flamm_index < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    '''For creating boxing gloves to be inventoried'''
    def __init__(
            self, 
            name, 
            weight = 10
            ):
        Product.__init__(self, name, weight = 10)
        
    def explode(self): # Overrides the product's explode method
        return "...it's a glove"
    
    def punch(self): # Measures power of punch using weight
        if self.weight < 5:
            return 'That tickles'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'

