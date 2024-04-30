#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def set_sides(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_angles(self):
        angle1 = math.degrees(
            math.acos(
                (self.side2**2 + self.side3**2 - self.side1**2)
                / (2 * self.side2 * self.side3)
            )
        )
        angle2 = math.degrees(
            math.acos(
                (self.side1**2 + self.side3**2 - self.side2**2)
                / (2 * self.side1 * self.side3)
            )
        )
        angle3 = 180 - angle1 - angle2
        return angle1, angle2, angle3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class RightAngled(Triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
        self.area = 0

    def calculate_area(self):
        if (
            self.side1**2 + self.side2**2 == self.side3**2
            or self.side1**2 + self.side3**2 == self.side2**2
            or self.side2**2 + self.side3**2 == self.side1**2
        ):
            self.area = 0.5 * self.side1 * self.side2
            return self.area
        else:
            return "Not a right-angled triangle"


if __name__ == "__main__":
    triangle = Triangle(3, 4, 5)
    print("Angles of the triangle:", triangle.calculate_angles())
    print("Perimeter of the triangle:", triangle.calculate_perimeter())

    right_triangle = RightAngled(3, 4, 5)
    print("Area of the right-angled triangle:", right_triangle.calculate_area())
