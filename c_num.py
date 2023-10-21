from math import atan2, cos, exp, log, sin
from typing import Self


class CNum:
    real_part: float = 0.0
    imaginary_part: float = 0.0

    def __init__(self, real_part: float = 0.0, imaginary_part: float = 0.0):
        self.imaginary_part = float(imaginary_part)
        self.real_part = float(real_part)

    def __str__(self) -> str:
        if self.real_part >= 0.0 and self.imaginary_part >= 0.0:
            return f'{self.real_part} + {self.imaginary_part} * i'
        if self.real_part < 0.0 and self.imaginary_part < 0.0:
            return f'-{abs(self.real_part)} - {abs(self.imaginary_part)} * i'
        if self.real_part < 0.0:
            return f'-{abs(self.real_part)} + {self.imaginary_part} * i'
        return f'{self.real_part} - {abs(self.imaginary_part)} * i'

    def __add__(self, other: Self | int | float) -> Self:
        if not (isinstance(other, float) or isinstance(other, int) or isinstance(other, CNum)):
            raise TypeError()

        if isinstance(other, CNum):
            return CNum(
                self.real_part + other.real_part,
                self.imaginary_part + other.imaginary_part
            )

        return CNum(self.real_part + other, self.imaginary_part)

    def __sub__(self, other: Self | float | int) -> Self:
        if not (isinstance(other, float) or isinstance(other, int) or isinstance(other, CNum)):
            raise TypeError()
        if isinstance(other, CNum):
            return CNum(
                self.real_part - other.real_part,
                self.imaginary_part - other.imaginary_part
            )

        return CNum(self.real_part - other, self.imaginary_part)

    def __mul__(self, other: Self | float | int) -> Self:
        if not (isinstance(other, float) or isinstance(other, int) or isinstance(other, CNum)):
            raise TypeError()

        if isinstance(other, CNum):
            new_real_part = (
                    self.real_part
                    * other.real_part
                    - self.imaginary_part
                    * other.imaginary_part
            )

            new_imaginary_part = (
                    self.real_part
                    * other.imaginary_part
                    + self.imaginary_part
                    * other.real_part
            )

            return CNum(new_real_part, new_imaginary_part)

        return CNum(other * self.real_part, other * self.imaginary_part)

    def __truediv__(self, other: Self | float | int) -> Self:
        if not (isinstance(other, float) or isinstance(other, int) or isinstance(other, CNum)):
            raise TypeError()

        if isinstance(other, CNum):
            if other.real_part or other.imaginary_part:
                raise ZeroDivisionError()

            divider = (
                    other.real_part ** 2
                    + other.imaginary_part ** 2
            )
            new_real_part = ((
                                     self.real_part
                                     * other.real_part
                                     + self.imaginary_part
                                     * other.imaginary_part
                             ) / divider
                             )
            new_imaginary_part = ((
                                          self.imaginary_part
                                          * other.real_part
                                          - self.real_part
                                          * other.imaginary_part
                                  ) / divider
                                  )

            return CNum(new_real_part, new_imaginary_part)

        if other:
            raise ZeroDivisionError()

        return CNum(self.real_part / other, self.imaginary_part / other)

    def __radd__(self, other: Self) -> Self:
        return self + other

    def __rsub__(self, other: Self | float | int) -> Self:
        return -self + other

    def __rmul__(self, other: Self | float | int) -> Self:
        return self * other

    def __abs__(self) -> float:
        return (self.real_part ** 2 + self.imaginary_part ** 2) ** 0.5

    def __eq__(self, other: Self) -> bool:
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part

    def __ne__(self, other: Self) -> bool:
        return self.real_part != other.real_part or self.imaginary_part != other.imaginary_part

    def __pow__(self, power: int | float | Self, modulo=None) -> Self:
        if not (isinstance(power, float) or isinstance(power, int) or isinstance(power, CNum)):
            raise TypeError()

        if isinstance(power, float) or isinstance(power, int):
            return abs(self) * CNum(cos(power * self.get_fi()), sin(power * self.get_fi()))

        return (self.__get_power_for_pow(power)).get_exp()

    def __neg__(self) -> Self:
        return CNum(-self.real_part, -self.imaginary_part)

    def get_log(self):
        return CNum(log(abs(self)), self.get_fi())

    def get_exp(self) -> Self:
        return exp(self.real_part) * CNum(cos(self.imaginary_part), sin(self.imaginary_part))

    def get_fi(self) -> float:
        return atan2(self.imaginary_part, self.real_part)

    def __get_power_for_pow(self, other: Self) -> Self:
        if not isinstance(other, CNum):
            raise TypeError()
        return self.get_log() * other

    @staticmethod
    def get_cnum_from_str(c_num: str) -> list[float]:
        sign: int = 1
        tmp = ''
        n = 0
        answer: list[float] = [0.0, 0.0]
        for elem in c_num:
            if elem in '1234567890.':
                tmp += elem
                continue

            if elem == "i" and answer[0] == 0:
                n = 1

            if elem == "i" and tmp == "" and '*' not in c_num:
                tmp = 1.0

            if elem in 'i-+*' and tmp != '':
                answer[n] = float(tmp) * sign
                tmp = ''
                n += 1
                sign = 1

            if elem == '-':
                sign = -1

        if tmp != '':
            answer[0] = float(c_num) * sign
        return answer

    def update_c_num(self, c_num: str):
        if 'i' in c_num:
            self.real_part, self.imaginary_part = self.get_cnum_from_str(c_num)
        else:
            self.real_part = float(c_num)
