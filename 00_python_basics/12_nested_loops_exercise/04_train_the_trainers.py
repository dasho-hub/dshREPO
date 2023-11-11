jury_count = int(input())
pres_counter = 0
command = input()
total_total_score = 0

while command != "Finish":
    presentation = command
    pres_counter += 1
    total_score = 0
    for _ in range(jury_count):
        total_score += float(input())

    avg_score = total_score / jury_count
    print(f"{presentation} - {avg_score :.2f}.")

    total_total_score += total_score
    command = input()

total_avg_score = total_total_score / (pres_counter * jury_count)
print(f"Student's final assessment is {total_avg_score :.2f}.")