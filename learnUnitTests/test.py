import unittest
from main import div_rem

class TestDivRem(unittest.TestCase):
    def test_div_rem(self):
        self.assertEqual(div_rem(0, 5), 0)
        self.assertEqual(div_rem(1, 15), 1)
        self.assertEqual(div_rem(15, 5), 0)

    def test_div_rem_exception(self):
        with self.assertRaises(ZeroDivisionError):
            div_rem(3, 0)

if __name__ == '__main__':
    unittest.main()