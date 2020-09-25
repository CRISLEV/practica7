import unittest
from Repartidor_main import testRepartidor

class test_repartidor(unittest.TestCase):

    def test(self):
        result = testRepartidor()
        self.assertIsNotNone(result)
        print(result)


if __name__ == '__main__':
    unittest.main()
