import unittest
from .solution import Solution
class TestSearchInsert(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    
    def test_target_exists(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 5), 2)

    def test_insert_middle(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)

    def test_insert_end(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 7), 4)

    def test_insert_start(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 0), 0)

    
    def test_single_element_smaller(self):
        self.assertEqual(self.solution.searchInsert([1], 0), 0)

    def test_single_element_larger(self):
        self.assertEqual(self.solution.searchInsert([1], 2), 1)

    
    def test_two_elements_middle(self):
        self.assertEqual(self.solution.searchInsert([1,3], 2), 1)

    def test_two_elements_end(self):
        self.assertEqual(self.solution.searchInsert([1,3], 4), 2)


if __name__ == '__main__':
    unittest.main()
