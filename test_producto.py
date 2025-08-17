import unittest
from producto import producto


class TestProducto(unittest.TestCase):
    def test_producto(self):
        self.assertEqual(producto(3, 4), 12)
        self.assertEqual(producto(9, 0), 0)
        self.assertEqual(producto(-1, -1), 1)


if __name__ == "__main__":
    unittest.main()
