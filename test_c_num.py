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

    def test_str(self):
        self.assertEqual(str(get_c_num('1')), '1.0 + 0.0 * i')
        self.assertEqual(str(get_c_num('-1')), '-1.0 + 0.0 * i')
        self.assertEqual(str(get_c_num('i')), '0.0 + 1.0 * i')
        self.assertEqual(str(get_c_num('-i')), '0.0 - 1.0 * i')
        self.assertEqual(str(get_c_num('-1-i')), '-1.0 - 1.0 * i')

    def test_get_c_num_from_str(self):
        self.assertEqual(str(get_c_num('1')), str(CNum(1)))
        self.assertEqual(str(get_c_num('1+i')), str(CNum(1, 1)))
        self.assertEqual(str(get_c_num('i')), str(CNum(0, 1)))
        self.assertEqual(str(get_c_num('-i')), str(CNum(0, -1)))
        self.assertEqual(str(get_c_num('1+')), str(CNum(1, 0)))
        self.assertEqual(str(get_c_num('i-')), str(CNum(0, 1)))
        self.assertEqual(str(get_c_num('-1')), str(CNum(-1, 0)))

    def test_update_c_num(self):
        a = get_c_num('1')
        a.update_c_num('i')
        self.assertEqual(str(a), str(CNum(0, 1)))
        a.update_c_num('2')
        self.assertEqual(str(a), str(CNum(2, 0)))

    def test_sum(self):
        self.assertEqual(str(self.a + self.b), str(self.c))

    def test_sub(self):
        self.assertEqual(str(self.a - self.b), str(self.i))

    def test_zero_divider_error(self):
        with self.assertRaises(ZeroDivisionError):
            a = self.a / self.g
            print(a)

        with self.assertRaises(ZeroDivisionError):
            a = self.a / 0
            print(a)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            a = self.a / '1'
            print(a)

        with self.assertRaises(TypeError):
            a = self.a + '1'
            print(a)

        with self.assertRaises(TypeError):
            a = self.a - '1'
            print(a)

        with self.assertRaises(TypeError):
            a = self.a * '1'
            print(a)

        with self.assertRaises(TypeError):
            a = self.a ** '1'
            print(a)

    def test_eq(self):
        self.assertEqual(self.a == get_c_num("1"), True)

    def test_ne(self):
        self.assertEqual(self.a != get_c_num("2"), True)

    def test_abs(self):
        self.assertEqual(abs(CNum(3, 4)), 5)


if __name__ == '__main__':
    unittest.main()
