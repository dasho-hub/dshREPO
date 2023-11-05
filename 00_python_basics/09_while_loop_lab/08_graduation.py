
student_name = input()
current_class = 1
sum_of_grades = 0
was_excluded = False
is_excluded = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        if was_excluded == False:
            was_excluded = True
        else:
            is_excluded = True
            break
        continue
    current_class += 1
    sum_of_grades += current_grade

if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    avg_grade = sum_of_grades / 12
    print(f"{student_name} graduated. Average grade: {avg_grade :.2f}")
