import math
tourney_count = int(input())
starting_points = int(input())

points_gained = 0
wins_count = 0

for _ in range(tourney_count):
    current_stage = input()

    if current_stage == "W":
        points_gained += 2000
        wins_count += 1
    elif current_stage == "F":
        points_gained += 1200
    elif current_stage == "SF":
        points_gained += 720

final_points = starting_points + points_gained
average_points = points_gained / tourney_count
percent_tourney_wins = wins_count / tourney_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_tourney_wins:.2f}%")