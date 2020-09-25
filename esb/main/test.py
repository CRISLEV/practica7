import unittest
from esb import testEsb

class test_repartidor(unittest.TestCase):

    def test(self):
        result = testEsb()
        self.assertIsNotNone(result)
        print(result)


if __name__ == '__main__':
    unittest.main()
