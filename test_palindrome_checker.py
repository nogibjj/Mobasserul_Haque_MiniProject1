import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome(self):
        # Test case 1: Simple palindrome
        self.assertTrue(is_palindrome("racecar"))
        
        # Test case 2: Simple non-palindrome
        self.assertFalse(is_palindrome("hello"))
        
        # Test case 3: Single character (always a palindrome)
        self.assertTrue(is_palindrome("a"))
        
        # Test case 4: Empty string (considered a palindrome)
        self.assertTrue(is_palindrome(""))
        
        # Test case 5: Palindrome with mixed cases
        self.assertTrue(is_palindrome("Madam"))
        
        # Test case 8: Another simple non-palindrome
        self.assertFalse(is_palindrome("python"))

if __name__ == "__main__":
    unittest.main()
