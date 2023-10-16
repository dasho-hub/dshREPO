import math

figure_type = input("choose and type square/rectangle/circle/triangle: ")
if figure_type == "square":
    square_side = float(input())
    square_area = square_side * square_side
    print(f"{square_area:.3f}")

elif figure_type == "rectangle":
    rectangle_side_a = float(input("side A length: "))
    rectangle_side_b = float(input("side B length: "))
    rectangle_area = rectangle_side_a * rectangle_side_b
    print(f"{rectangle_area:.3f}")

elif figure_type == "circle":
    circle_radius = float(input("radius length: "))
    circle_area = math.pi * (circle_radius * circle_radius)
    print(f"{circle_area:.3f}")

elif figure_type == "triangle":
    triangle_side = float(input("side A length: "))
    triangle_height = float(input("height length: "))
    triangle_area = (triangle_side / 2) * triangle_height
    print(f"{triangle_area:.3f}")
else:
    print("invalid input")