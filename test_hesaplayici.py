import unittest
from hesaplayici import topla

class TestHesaplayici(unittest.TestCase):
    def test_topla(self):
        self.assertEqual(topla(2, 3), 5)
        self.assertEqual(topla(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()