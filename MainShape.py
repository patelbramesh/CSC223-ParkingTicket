"""
File Name: MainShape.py
Author: Bramesh Patel
Date: March 13, 2026

Description:
This program tests the Shapes inheritance hierarchy.
It demonstrates polymorphism, dynamic method resolution,
and automatic area recalculation using property setters.
"""

from shapes import Circle, Rectangle, Square


def main():

    shapes = [
        Circle(0, 0, 4, "Circle_1"),
        Circle(1, 1, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(20, 30, "Rectangle_2"),
        Square(10, "Square")
    ]

    print("--- Polymorphism check ---")

    for shape in shapes:
        print(f"{shape.name} Area = {shape.area:.5f}")

    print("\n--- Getter/setter check ---")

    # Circle test
    c = shapes[0]
    print(f"{c.name} Current: {c.radius} {c.area:.5f}")
    c.radius *= 2
    print(f"{c.name} Doubled: {c.radius} {c.area:.5f}")

    # Rectangle test
    r = shapes[2]
    print(f"{r.name} Current: {r.length} {r.width} {r.area:.5f}")
    r.length *= 2
    r.width *= 2
    print(f"{r.name} Doubled: {r.length} {r.width} {r.area:.5f}")

    # Square test
    s = shapes[4]
    print(f"{s.name} Current: {s.side} {s.area:.5f}")
    s.side *= 2
    print(f"{s.name} Doubled: {s.side} {s.area:.5f}")


if __name__ == "__main__":
    main()