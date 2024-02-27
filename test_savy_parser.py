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
        Parser(input)

    def test_conjunction1(self):
        input = "(A&!(A&C))"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_conjunction2(self):
        input = "A&B&C"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_conjunction3(self):
        input = "A&B&C&D"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_conjunction_negation(self):
        input = "Z & !(A & B)"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_disjunction(self):
        input = "C | D"
        print("___________________________________________________________________")
        print(input)
        Parser(input)
    
    def test_disjunction1(self):
        input = "A | (D | E)"
        print("___________________________________________________________________")
        print(input)
        Parser(input)
    
    def test_disjunction2(self):
        input = "B & C | D"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_conditional(self):
        input = "A => B"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_conditional1(self):
        input = "A => (B | C)"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_conditional2(self):
        input = "A => !B=>C"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_biconditional(self):
        input = "A <=> B"
        print("___________________________________________________________________")
        print(input)
        Parser(input)
    
    def test_biconditional1(self):
        input = " A <=> B <=> C"
        print("___________________________________________________________________")
        print(input)
        Parser(input)
    
    def test_biconditional2(self):
        input = " A <=> !(B <=> C)"
        print("___________________________________________________________________")
        print(input)
        Parser(input)

    def test_unique_variable_tokens(self):
        input = "A & (B | C)"
        parser = Parser(input)
        actual_variable_list = parser.variable_list
        expected_variable_list = ['A', 'B', 'C']
        self.assertCountEqual(
            actual_variable_list,
            expected_variable_list,
            f"expected {expected_variable_list}, but got {actual_variable_list} instead."
        )

    def test_unique_variable_tokens2(self):
        input = "A & (B | A)"
        parser = Parser(input)
        actual_variable_list = parser.variable_list
        expected_variable_list = ['B', 'A']
        self.assertCountEqual(
            actual_variable_list,
            expected_variable_list,
            f"expected {expected_variable_list}, but got {actual_variable_list} instead."
        )

    def test_truth_table_size(self):
        input = "A & (B | A)"
        parser = Parser(input)
        truth_table = parser.truth_table

        expected_num_rows = 4
        expected_num_cols = 3

        actual_num_rows, actual_num_cols = truth_table.shape

        self.assertEqual(
            actual_num_rows,
            expected_num_rows,
            f"expected {expected_num_rows} rows, but got {actual_num_rows} rows instead."
        )

        self.assertEqual(
            actual_num_cols,
            expected_num_cols,
            f"expected {expected_num_cols} cols, but got {actual_num_cols} cols instead."
        )


    def test_truth_table_size(self):
        input = "A & (B | A) | C & C <=> d"
        parser = Parser(input)
        truth_table = parser.truth_table

        expected_num_rows = 16
        expected_num_cols = 5

        actual_num_rows, actual_num_cols = truth_table.shape

        self.assertEqual(
            actual_num_rows,
            expected_num_rows,
            f"expected {expected_num_rows} rows, but got {actual_num_rows} rows instead."
        )

        self.assertEqual(
            actual_num_cols,
            expected_num_cols,
            f"expected {expected_num_cols} cols, but got {actual_num_cols} cols instead."
        )

    
    def test_populate_truth_table(self):
        input = "A & B & C & D"
        parser = Parser(input)


if __name__ == '__main__':
    unittest.main()

