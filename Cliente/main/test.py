import unittest
from Client import testClient

class test_client(unittest.TestCase):

    def test(self):
        result = testClient()
        self.assertIsNotNone(result)
        print(result)


if __name__ == '__main__':
    unittest.main()
