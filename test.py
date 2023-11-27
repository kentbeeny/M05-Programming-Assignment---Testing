#Kent Beeny
#SDEV220
#M05 Programming Assignment - Testing


import unittest
from fractions import Fraction

from my_sum import sum

#test the sum of integers in a list
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    #test the sum of fractions in a list
    def test_list_fraction(self):
            """
            Test that it can sum a list of fractions
            """
            data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
            result = sum(data)
            self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

#The first test is testing that the sum of the 3 integers in the list (1,2,3) 
    #match the expected results (6) and they do so it passes.
#The second test is testing that the sum of the fractions in the list
    #(1/4, 1/4, and 2/5) match the given expected result (1) and they do not,
    #so this test fails.
