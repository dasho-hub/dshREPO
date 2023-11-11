house_width = float(input())
house_length = float(input())
house_roof_height = float(input())

door_area = 1.2 * 2
front_back_wall_area = ((house_width * house_width) * 2) - door_area

side_window_area = 1.5 * 1.5
side_wall_area = ((house_width * house_length) * 2) - (side_window_area * 2)

green_paint_area = front_back_wall_area + side_wall_area
green_paint = green_paint_area / 3.4

############## ROOF ################

roof_side_area = (house_width * house_length) * 2
roof_frontback_area = (house_width * house_roof_height / 2) * 2

red_paint_area = roof_side_area + roof_frontback_area
red_paint = red_paint_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")