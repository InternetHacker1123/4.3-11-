#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class Function(ABC):
    @abstractmethod
    def calculate_y(self, x):
        pass

    @abstractmethod
    def display_result(self, result):
        pass


class Ellipse(Function):
    def calculate_y(self, x):
        a = 2
        b = 1
        y = (b**2 * (1 - (x**2 / a**2))) ** 0.5
        return y

    def display_result(self, result):
        print(f"Result for Ellipse: y = {result}")


class Hyperbola(Function):
    def calculate_y(self, x):
        a = 2
        b = 1
        y = (b**2 * ((x**2 / a**2) - 1)) ** 0.5
        return y

    def display_result(self, result):
        print(f"Result for Hyperbola: y = {result}")


def main():
    x_value = 1.5

    ellipse = Ellipse()
    y_ellipse = ellipse.calculate_y(x_value)
    ellipse.display_result(y_ellipse)

    hyperbola = Hyperbola()
    y_hyperbola = hyperbola.calculate_y(x_value)
    hyperbola.display_result(y_hyperbola)


if __name__ == "__main__":
    main()
