from c_num import CNum
from fraction import Fraction


def get_fraction(a):
    return Fraction(a)


def get_c_num(a):
    x = CNum()
    x = CNum(x.get_cnum_from_str(a)[0], x.get_cnum_from_str(a)[1])
    return x


def main():
    a = get_c_num(input())
    print(a)


if __name__ == '__main__':
    main()
