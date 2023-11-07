space_a = int(input())
space_b = int(input())
space_c = int(input())

space_volume = space_a * space_b * space_c

command = input()

while command != "Done":
    space_taken = int(command)
    space_volume -= space_taken
    if space_volume < 0:
        break
    command = input()

if space_volume >= 0:
    print(f"{space_volume} Cubic meters left.")

if space_volume < 0:
    print(f"No more free space! You need {abs(space_volume)} Cubic meters more.")
