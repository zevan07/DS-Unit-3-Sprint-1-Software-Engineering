from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products(num_products = 30):
    '''Generates products for inventory.'''
    i = 0
    products = []
    while i < num_products:
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5, 101)
        weight = random.randint(5, 101)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammability))
        i += 1
    return products

def inventory_report(products):
    '''Generates a report of inventory.'''
    names = []
    price_total = 0
    weight_total = 0
    flam_total = 0
    products_total = len(products)
    
    for item in products:
        if item.name not in names:
            names.append(item.name)
        price_total += item.price
        weight_total += item.weight
        flam_total += item.flammability
        
    avg_price = price_total / products_total
    avg_weight = weight_total / products_total
    avg_flammability = flam_total / products_total
    return f'Number of Unique names: {len(names)} Avg price: {avg_price} Avg weight: {avg_weight} Avg flammability: {avg_flammability}'

if __name__ == '__main__':
    print(inventory_report(generate_products()))