#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test stealability function."""
        prod = Product('Test Product', flammability = .6, price= 50, weight = 30)
        self.assertEqual(prod.explode(), '...boom!')
        self.assertEqual(prod.stealability(), 'Very stealable!')

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme report is accurate."""
    def test_default_num_products(self):
        """Test to ensure 30 products in report."""
        report = generate_products()
        self.assertEqual(len(report), 30)

    def test_legal_names(self):
        """Making sure names for products are legal."""
        products = generate_products()
        NAMES = ADJECTIVES + NOUNS
        for product in products:
            for word in product.name.split():
                self.assertIn(word, NAMES)



if __name__ == '__main__':
    unittest.main()