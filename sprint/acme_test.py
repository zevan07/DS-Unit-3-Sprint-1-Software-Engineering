import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        p1 = Product('prod1')
        p2 = Product('prod2', 5, 20)
        p3 = Product('prod3', 20, 20)
        p4 = Product('prod4', 25, 20)

        self.assertEqual(p1.stealability(), "Kinda stealable.")
        self.assertEqual(p2.stealability(), "Not so stealable...")
        self.assertEqual(p3.stealability(), "Very stealable!")
        self.assertEqual(p4.stealability(), "Very stealable!")

    def test_explode(self):
        p1 = Product('prod1', 1, 19, 0.5)
        p2 = Product('prod2', 1, 21, 0.5)
        p3 = Product('prod3', 1, 48, 1)
        p4 = Product('prod4', 1, 50, 2)

        self.assertEqual(p1.explode(), "...fizzle.")
        self.assertEqual(p2.explode(), "...boom!")
        self.assertEqual(p3.explode(), "...boom!")
        self.assertEqual(p4.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        for product in generate_products():
            name = product.name
            self.assertEqual(name.count(' '), 1)
            adj, noun = name.split(' ')
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
