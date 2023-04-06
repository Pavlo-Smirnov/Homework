"""I didn't make a phonebook, so I use a task #3 from the 16th lesson"""
import unittest
import products

class ProductsTestCase(unittest.TestCase):

    def test_income(self):
        income = products.store.get_income()
        prediction = 9.000000000000004
        self.assertEqual(income, prediction)

    def test_get_all_products(self):
        expected = products.store.get_all_products()
        prediction = "Football T-Shirt", "Ramen"
        self.assertNotEqual(expected, prediction)

    def test_get_product_info(self):
        info = products.store.get_product_info()
        prediction = 'Sport', "Football T-Shirt"
        self.assertEqual(info, prediction)

if __name__ == "__main__":
    unittest.main()