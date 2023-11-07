"""
Importing unittest module
"""
import unittest
class Calculator:
    """
    A simple calculator class.
    """
    print("Jeevan")
    print("HI")
    print("updated file")
    def add(self, x_value, y_value):
        """
        Add two numbers.
        """
        return x_value + y_value
    def subtract(self, x_value, y_value):
        """
        Subtract two numbers.
        """
        return x_value - y_value
    def multiply(self, x_value, y_value):
        """
        Multiply two numbers.
        """
        return x_value * y_value
    def divide(self, x_value, y_value):
        """
        Divide two numbers.
        """
        if y_value == 0:
            raise ValueError("Division by zero is not allowed")
        return x_value / y_value

class CalculatorTest(unittest.TestCase):
    """
    Unit tests for the Calculator class.
    """

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """
        Test the add method.
        """
        self.assertEqual(10, self.calc.add(2, 7), "The addition is wrong")

    def test_subtract(self):
        """
        Test the subtract method.
        """
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        """
        Test the multiply method.
        """
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        """
        Test the divide method.
        """
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__== '_main_':
    unittest.main()
