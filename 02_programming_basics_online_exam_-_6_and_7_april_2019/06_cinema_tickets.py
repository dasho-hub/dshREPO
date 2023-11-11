command = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while command != "Finish":
    percentage_full = 0
    current_movie_tickets = 0
    movie_name = command
    free_tickets = int(input())

    for _ in range(free_tickets):
        ticket_type = input()
        if ticket_type == "standard":
            total_tickets += 1
            current_movie_tickets += 1
            standard_tickets += 1
        elif ticket_type == "student":
            total_tickets += 1
            current_movie_tickets += 1
            student_tickets += 1
        elif ticket_type == "kid":
            total_tickets += 1
            current_movie_tickets += 1
            kid_tickets += 1
        elif ticket_type == "End":
            break

    percentage_full = current_movie_tickets / free_tickets * 100
    print(f"{movie_name} - {percentage_full :.2f}% full.")
    command = input()

standard_tickets_percentage = standard_tickets / total_tickets * 100
student_tickets_percentage = student_tickets / total_tickets * 100
kid_tickets_percentage = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percentage :.2f}% student tickets.")
print(f"{standard_tickets_percentage :.2f}% standard tickets.")
print(f"{kid_tickets_percentage :.2f}% kids tickets.")
