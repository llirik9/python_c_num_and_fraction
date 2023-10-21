import unittest
from c_num import CNum
from main import get_c_num


class MyTestCase(unittest.TestCase):
    a = CNum(1, 0)
    b = CNum(0, 1)
    c = CNum(1, 1)
    d = CNum(-1, 0)
    e = CNum(0, -1)
    f = CNum(-1, -1)
    g = CNum(0, 0)
    h = CNum(-1, 1)
    i = CNum(1, -1)

    def test_get_c_num_from_str(self):
        self.assertEqual(str(get_c_num('1')), str(CNum(1)))
        self.assertEqual(str(get_c_num('1+i')), str(CNum(1, 1)))
        self.assertEqual(str(get_c_num('i')), str(CNum(0, 1)))
        self.assertEqual(str(get_c_num('-i')), str(CNum(0, -1)))
        self.assertEqual(str(get_c_num('1+')), str(CNum(1, 0)))
        self.assertEqual(str(get_c_num('i-')), str(CNum(0, 1)))


if __name__ == '__main__':
    unittest.main()
