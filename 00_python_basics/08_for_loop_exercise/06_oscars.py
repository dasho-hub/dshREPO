actor_name = str(input())
starting_points = float(input())
judge_count = int(input())

points_needed = 1250.5
current_points = 0

for _ in range(judge_count):
    judge_name = input()
    judge_points = float(input())
    judge_name_length = len(judge_name)
    current_points += judge_name_length * judge_points / 2
    if current_points + starting_points >= points_needed:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {(current_points + starting_points):.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {(points_needed - (current_points + starting_points)):.1f} more!")