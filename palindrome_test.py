"""
Test for Anagram Class
"""
try:
    from palindrome import Palindrome
except ImportError:
    raise SystemExit('palindrome.py is not exist!')

import unittest

class PalindromeTests(unittest.TestCase):
    def test_no_matches(self):
        self.assertEqual(
            False,
            Palindrome().is_palindrome_of('bowery', 'bowfin')
        )

    def test_detect_simple_anagram(self):
        self.assertEqual(
            True,
            Palindrome().is_palindrome_of('adders', 'sredda')
        )

if __name__ == '__main__':
    unittest.main()