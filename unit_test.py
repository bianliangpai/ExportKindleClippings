import unittest
from exportkindleclippings import is_similarly

class TestStringMethods(unittest.TestCase):

    def test_is_similarly(self):
        self.assertTrue(is_similarly('abc', 'abc'))
        self.assertTrue(is_similarly('abc', 'abcd'))
        self.assertTrue(is_similarly('abcd', 'abc'))

        self.assertFalse(is_similarly('abcd', 'abd'))
        self.assertFalse(is_similarly('abd', 'abcd'))
        self.assertFalse(is_similarly('abcd', 'abce'))
        self.assertFalse(is_similarly('abcd', 'efgh'))

if __name__ == '__main__':
    unittest.main()