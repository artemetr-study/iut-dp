import unittest

from lw_2.affine import Affine


class AffineTestCase(unittest.TestCase):
    def test_encode(self):
        affine = Affine(3, 4, 991)
        test_message = 'This is the only test message with 123 numbers, and !@# symbols'
        self.assertNotEqual(test_message, affine.encode(test_message))
        self.assertEqual(test_message, affine.decode(affine.encode(test_message)))


if __name__ == '__main__':
    unittest.main()
