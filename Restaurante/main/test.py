import unittest
from Restaurante import testRestaurante

class test_restaurante(unittest.TestCase):

    def test(self):
        result = testRestaurante()
        self.assertIsNotNone(result)
        print(result)


if __name__ == '__main__':
    unittest.main()
