import unittest

from main import get_fraction
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_type_error(self):
        a = get_fraction('1')
        b = '1'
        with self.assertRaises(TypeError):
            c = a / b
            print(str(c))
        with self.assertRaises(TypeError):
            c = a * b
            print(str(c))
        with self.assertRaises(TypeError):
            c = get_fraction([1, 2])
            print((str(c)))
        with self.assertRaises(TypeError):
            c = a + b
            print(str(c))
        with self.assertRaises(TypeError):
            c = b + a
            print(str(c))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            get_fraction('./')

        with self.assertRaises(ValueError):
            get_fraction('abba')

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            get_fraction((1, 0))

        with self.assertRaises(ZeroDivisionError):
            get_fraction('1/0')

    def test_type(self):
        self.assertEqual(str(get_fraction("1")), str(Fraction(1)))
        self.assertEqual(str(get_fraction((1, -1))), str(Fraction((-1, 1))))
        self.assertEqual(str(get_fraction(('1', '-1'))), str(Fraction((-1, 1))))
        self.assertEqual(str(get_fraction("0.5")), str(Fraction(0.5)))
        self.assertEqual(str(get_fraction("0.5/1")), str(Fraction(0.5)))
        self.assertEqual(str(get_fraction("0.5/1")), str(Fraction(0.5)))
        self.assertEqual(str(get_fraction("0,5\\1")), str(Fraction(0.5)))
        self.assertEqual(str(get_fraction(1.0)), str(Fraction(1)))

    def test_answer(self):
        a = Fraction((1, 2))
        b = 2
        c = -2
        self.assertEqual(str(a/b), str(Fraction(0.25)))
        self.assertEqual(str(b/a), str(Fraction(4)))
        self.assertEqual(str(a*b), str(Fraction(1)))
        self.assertEqual(str(a+b), str(Fraction((5, 2))))
        self.assertEqual(str(a-b), str(Fraction(-1.5)))
        self.assertEqual(str(a**b), str(Fraction(0.25)))
        self.assertEqual(str(a**c), str(Fraction(4)))


if __name__ == '__main__':
    unittest.main()
