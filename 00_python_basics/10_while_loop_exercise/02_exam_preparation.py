max_number_of_fails = int(input())
problems_solved = 0
problems_failed = 0
sum_grades = 0
last_problem = ""
is_failed = True

while problems_failed < max_number_of_fails:
    current_problem = input()
    if current_problem == "Enough":
        is_failed = False
        break
    current_grade = int(input())
    if current_grade <=4:
        problems_failed += 1
    sum_grades += current_grade
    problems_solved += 1
    last_problem = current_problem

if is_failed:
    print(f"You need a break, {max_number_of_fails} poor grades.")
else:
    print(f"Average score: {sum_grades / problems_solved :.2f}")
    print(f"Number of problems: {problems_solved}")
    print(f"Last problem: {last_problem}")