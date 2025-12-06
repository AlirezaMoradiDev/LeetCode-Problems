import unittest
import solution   # اگر فایل اسمش چیز دیگه است اصلاح کن

class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self.sol = solution()

    def test_positive_palindrome(self):
        self.assertTrue(self.sol.isPalindrome(121))
        self.assertTrue(self.sol.isPalindrome(0))
        self.assertTrue(self.sol.isPalindrome(9999))
        self.assertTrue(self.sol.isPalindrome(1221))

    def test_negative_not_palindrome(self):
        self.assertFalse(self.sol.isPalindrome(123))
        self.assertFalse(self.sol.isPalindrome(10))
        self.assertFalse(self.sol.isPalindrome(1231))

    def test_negative_numbers(self):
        self.assertFalse(self.sol.isPalindrome(-121))
        self.assertFalse(self.sol.isPalindrome(-1))
        self.assertFalse(self.sol.isPalindrome(-12321))

    def test_single_digit(self):
        self.assertTrue(self.sol.isPalindrome(7))
        self.assertTrue(self.sol.isPalindrome(3))

    def test_large_numbers(self):
        self.assertTrue(self.sol.isPalindrome(123454321))
        self.assertFalse(self.sol.isPalindrome(123456789))

if __name__ == '__main__':
    unittest.main()