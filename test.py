import unittest
from Calculator import calculator

class TestCalculator(unittest.TestCase):

    def test_Addition(self):
        self.assertEqual(calculator(3,2,"+"),5)
    
    def test_Subtraction(self):
        self.assertEqual(calculator(3,2,"-"),1)

    def test_Division(self):
        self.assertEqual(calculator(3,2,"/"),1.5)

    def test_Multiplication(self):
        self.assertEqual(calculator(3,2,"*"),6)
    

if __name__ == '__main__':
    unittest.main()