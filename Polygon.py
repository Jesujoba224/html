"""Polygon area calculator using OOP concepts.

Classes:
- Polygon (abstract base)
- Triangle (supports base+height or 3 sides (Heron's formula))
- Rectangle
- Square
- RegularPolygon (n-sided regular polygon)

Run this file directly for an interactive demo and examples.
"""

from __future__ import annotations
import math
from typing import Optional


class Polygon:
    """Abstract base class for polygons."""

    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self) -> float:
        raise NotImplementedError("Subclasses must implement perimeter()")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class Triangle(Polygon):
    """Triangle: can be constructed with base and height, or with three sides (a, b, c).

    Examples:
        Triangle(base=4, height=3)
        Triangle(a=3, b=4, c=5)
    """

    def __init__(self, *, base: Optional[float] = None, height: Optional[float] = None,
                 a: Optional[float] = None, b: Optional[float] = None, c: Optional[float] = None):
        self.base = base
        self.height = height
        self.a = a
        self.b = b
        self.c = c

        if (a is None or b is None or c is None) and (base is None or height is None):
            raise ValueError("Provide either (base and height) or (a, b, c) side lengths")

    def area(self) -> float:
        if self.base is not None and self.height is not None:
            return 0.5 * self.base * self.height
        # Heron's formula
        a, b, c = float(self.a), float(self.b), float(self.c)
        s = 0.5 * (a + b + c)
        if s <= a or s <= b or s <= c:
            raise ValueError("Invalid triangle side lengths")
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def perimeter(self) -> float:
        if self.a is not None and self.b is not None and self.c is not None:
            return self.a + self.b + self.c
        if self.base is not None and self.height is not None:
            # Perimeter unknown; return base as a partial indicator
            return float(self.base)
        raise ValueError("Insufficient data for perimeter")

    def __str__(self) -> str:
        return f"Triangle(area={self.area():.4f}, perimeter={self.perimeter():.4f})"


class Rectangle(Polygon):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area():.4f})"


class Square(Rectangle):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width}, area={self.area():.4f})"


class RegularPolygon(Polygon):
    """Regular polygon with n sides of equal length."""

    def __init__(self, n_sides: int, side_length: float):
        if n_sides < 3:
            raise ValueError("A polygon must have at least 3 sides")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.n = int(n_sides)
        self.s = float(side_length)

    def perimeter(self) -> float:
        return self.n * self.s

    def area(self) -> float:
        # Formula: (n * s^2) / (4 * tan(pi/n))
        return (self.n * (self.s ** 2)) / (4.0 * math.tan(math.pi / self.n))

    def __str__(self) -> str:
        return f"RegularPolygon(n={self.n}, side={self.s}, area={self.area():.4f})"


# Utility helpers for CLI
def _read_positive_number(prompt: str) -> float:
    while True:
        try:
            v = float(input(prompt))
            if v <= 0:
                print("Please enter a positive number.")
                continue
            return v
        except ValueError:
            print("Invalid number. Try again.")


def demo():
    print("Polygon Area Calculator (OOP demo)")
    print("Choose polygon:")
    print("1) Triangle (base & height)")
    print("2) Triangle (3 sides)")
    print("3) Rectangle")
    print("4) Square")
    print("5) Regular polygon (n sides)")
    choice = input("Enter choice (1-5): ").strip()

    try:
        if choice == "1":
            b = _read_positive_number("Base: ")
            h = _read_positive_number("Height: ")
            t = Triangle(base=b, height=h)
            print(f"Area = {t.area():.4f}")
        elif choice == "2":
            a = _read_positive_number("Side a: ")
            b = _read_positive_number("Side b: ")
            c = _read_positive_number("Side c: ")
            t = Triangle(a=a, b=b, c=c)
            print(f"Area = {t.area():.4f}")
            print(f"Perimeter = {t.perimeter():.4f}")
        elif choice == "3":
            w = _read_positive_number("Width: ")
            h = _read_positive_number("Height: ")
            r = Rectangle(w, h)
            print(f"Area = {r.area():.4f}")
            print(f"Perimeter = {r.perimeter():.4f}")
        elif choice == "4":
            s = _read_positive_number("Side: ")
            sq = Square(s)
            print(f"Area = {sq.area():.4f}")
            print(f"Perimeter = {sq.perimeter():.4f}")
        elif choice == "5":
            n = int(_read_positive_number("Number of sides (integer >=3): "))
            side = _read_positive_number("Side length: ")
            poly = RegularPolygon(n, side)
            print(f"Area = {poly.area():.4f}")
            print(f"Perimeter = {poly.perimeter():.4f}")
        else:
            print("Unknown choice. Exiting.")
    except Exception as exc:
        print("Error:", exc)


if __name__ == "__main__":
    # Small examples
    print("Examples:")
    print(Triangle(a=3, b=4, c=5))
    print(Rectangle(4, 5))
    print(Square(3))
    print(RegularPolygon(6, 2))

    # Run interactive demo
    while True:
        demo()
        again = input("Calculate another? (y/N): ").strip().lower()
        if again != "y":
            print("Goodbye")
            break
