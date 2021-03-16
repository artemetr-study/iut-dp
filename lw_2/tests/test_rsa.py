import unittest

from lw_2.rsa import Rsa


class RsaTestCase(unittest.TestCase):
    def test_encode(self):
        rsa = Rsa(103, 331)
        test_message = 'This is the only test message with 123 numbers, and !@# symbols'
        self.assertNotEqual(test_message, rsa.encode(test_message))
        self.assertEqual(test_message, rsa.decode(rsa.encode(test_message)))


if __name__ == '__main__':
    unittest.main()
