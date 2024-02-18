import unittest
from savy_parser import *

class TestSavyParser(unittest.TestCase):

    def test_basic(self):
        input = "(A)"
        print("___________________________________________________________________")
        print(input)
        parser = Parser(input)

    #Todo put in failure case
    
    def test_conjunction(self):
        input = "(!A&B)"
        print("___________________________________________________________________")
        print(input)
        parser = Parser(input)

    def test_conjunction1(self):
        input = "(A&!(A&C))"
        print("___________________________________________________________________")
        print(input)
        parser = Parser(input)

    def test_conjunction2(self):
        input = "A&B&C"
        print("___________________________________________________________________")
        print(input)
        parser = Parser(input)

if __name__ == '__main__':
    unittest.main()

