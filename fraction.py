from typing import Self


class Fraction:
    quotient: int = 0
    banner: int = 1

    def __init__(self, fraction: float | int | tuple[int, int] | str = 0.1):
        if isinstance(fraction, int):
            self.__get_fraction_from_int(fraction)
            return

        if isinstance(fraction, float):
            if int(fraction) == fraction:
                self.__get_fraction_from_int(int(fraction))
                return
            self.__get_fraction_from_float(fraction)
            return

        if isinstance(fraction, tuple):
            self.__get_fraction_from_tuple(fraction)
            return

        if isinstance(fraction, str):
            self.__get_fraction_from_str(fraction)
            return

        raise TypeError(f"{type(fraction)} don't to conversation to Fraction")

    def __str__(self) -> str:
        return f'{self.quotient}/{self.banner}'

    def __add__(self, other: Self | int | float) -> Self:
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction)):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")

        if isinstance(other, int) or isinstance(other, float):
            other = Fraction(fraction=other)

        answer = Fraction((
            self.quotient * other.banner + other.quotient * self.banner,
            self.banner * other.banner
        ))

        answer.update_fraction()

        return answer

    def __radd__(self, other) -> Self:
        return self + other

    def __sub__(self, other) -> Self:
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction)):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")

        if isinstance(other, int) or isinstance(other, float):
            other = Fraction(other)

        answer = Fraction((
            self.quotient * other.banner - other.quotient * self.banner,
            self.banner * other.banner
        ))

        answer.update_fraction()

        return answer

    def __rsub__(self, other) -> Self:
        return -self + other

    def __mul__(self, other) -> Self:
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction)):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")

        if isinstance(other, int) or isinstance(other, float):
            other = Fraction(other)

        answer = Fraction((
            self.quotient * other.quotient,
            self.banner * other.banner
        ))

        answer.update_fraction()

        return answer

    def __rmul__(self, other) -> Self:
        return self * other

    def __neg__(self) -> Self:
        return Fraction((-self.quotient, self.banner))

    def __truediv__(self, other: int | float | Self) -> Self:
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction)):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")

        if isinstance(other, int) or isinstance(other, float):
            other = Fraction(other)

        other.reversed()
        answer = self * other
        other.reversed()
        answer.update_fraction()
        return answer

    def __rtruediv__(self, other):
        if not (isinstance(other, int) or isinstance(other, float) or isinstance(other, Fraction)):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")

        if isinstance(other, int) or isinstance(other, float):
            other = Fraction(fraction=other)

        self.reversed()
        answer = self * other
        self.reversed()
        answer.update_fraction()
        return answer

    def __pow__(self, power: int, modulo=None) -> Self:
        if not isinstance(power, int):
            raise TypeError(f"{type(power)} is not int")

        if not power:
            return Fraction(1)

        answer = Fraction()

        answer.banner = self.banner ** abs(power)
        answer.quotient = self.quotient ** abs(power)
        answer.update_fraction()

        if power < 0:
            answer.reversed()

        return answer

    def __search_divider(self) -> int:
        min_i = abs(min(self.banner, self.quotient))
        for i in range(2, min_i + 1):
            if not (self.banner % i) and not (self.quotient % i):
                return i
        return 0

    def update_fraction(self):
        divider = self.__search_divider()

        while divider:
            self.banner = self.banner // divider
            self.quotient = self.quotient // divider
            divider = self.__search_divider()

        if self.banner < 0:
            self.banner = -self.banner
            self.quotient = -self.quotient
            self.update_fraction()

    def __get_fraction_from_float(self, other: float):
        whole_part = int(other)
        fraction_part = other - whole_part

        banner = 10 ** (len(str(fraction_part)) - 2)
        if int(fraction_part * banner) != fraction_part * banner:
            raise TypeError

        quotient = other * banner

        self.banner = banner
        self.quotient = int(quotient)
        self.update_fraction()

    def __get_fraction_from_int(self, other: int):
        if not isinstance(other, int):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")
        self.banner = 1
        self.quotient = other

    def __get_fraction_from_tuple(self, other: tuple):
        if len(other) != 2:
            raise ValueError

        if (
                not (isinstance(other[0], int) and isinstance(other[1], int))
                and not (isinstance(other[0], str) and isinstance(other[1], str))
        ):
            raise TypeError(f"{type(other)} don't to conversation to Fraction")

        if not other[1]:
            raise ZeroDivisionError

        if other[1] == '0':
            raise ZeroDivisionError

        if isinstance(other[0], str) and isinstance(other[1], str):
            self.quotient = int(other[0])
            self.banner = int(other[1])
            self.update_fraction()
            return

        self.quotient = other[0]
        self.banner = other[1]
        self.update_fraction()

    def __get_fraction_from_str(self, other: str):
        if not other:
            raise ValueError

        for elem in other:
            if elem not in '1234567890-\\/|.,':
                raise ValueError

        for elem in '0123456789':
            if elem in other:
                break
        else:
            raise ValueError

        if '/' in other or '|' in other or '\\' in other:
            self.__get_fraction_from_str_with_slash(other)
            return

        if '.' not in other and ',' not in other:
            self.__get_fraction_from_int(int(other))
            return

        if other.count('.') + other.count(',') > 1:
            raise ValueError

        if other.count(',') == 1:
            other = other.replace(',', '.')

        self.__get_fraction_from_float(float(other))

    def __get_fraction_from_str_with_slash(self, other: str):
        if other.count('\\') + other.count('|') + other.count('/') > 1:
            raise ValueError

        answer = tuple((0, 1))

        for i in '/\\|':
            if other.count(i):
                answer = tuple(other.split(i))

        if '.' in other or ',' in other:
            final_answer = Fraction(answer[0]) / Fraction(answer[1])
            self.banner = final_answer.banner
            self.quotient = final_answer.quotient
            return

        self.__get_fraction_from_tuple(answer)

    def reversed(self):
        tmp = self.banner
        self.banner = self.quotient
        self.quotient = tmp
        self.update_fraction()
