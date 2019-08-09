from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for num in range(num_products):
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        product = Product(name, price, weight, flammability)
        products.append(product)
    return products


def inventory_report(products):
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    length = len(products)
    price = 0
    weight = 0
    flammability = 0
    # TODO - your code! Loop over the products to calculate the report.
    for product in products:
        price += product.price
        weight += product.weight
        flammability += product.flammability
    print('Unique product names:', length)
    print('Average price:', price/length)
    print('Average weight:', weight/length)
    print('Average flammability:', flammability/length)


if __name__ == '__main__':
    inventory_report(generate_products())
