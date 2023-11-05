goal_steps = 10000

steps_taken = 0

while steps_taken < goal_steps:
    current_steps = input()
    if current_steps == "Going home":
        current_steps = int(input())
        steps_taken += current_steps
        break
    steps_taken += int(current_steps)

if steps_taken >= goal_steps:
    print(f"Goal reached! Good job!")
    print(f"{steps_taken - goal_steps} steps over the goal!")
else:
    print(f"{goal_steps - steps_taken} more steps to reach goal.")
