import unittest
from cash_register import change

class CashRegister(unittest.TestCase):
    def test_input(self):
        self.assertGreaterEqual(10, 5, "The amount paid is not equal or greater than the amount due.")


if __name__ == "__main__": 
    unittest.main()
