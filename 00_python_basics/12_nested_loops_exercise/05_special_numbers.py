number = int(input())
is_special = False
first_number = ""
second_number = ""
third_number = ""
fourth_number = ""

for i in range(1111, 9999 + 1):
    num_as_string = str(i)
    first_number = int(num_as_string[0])
    second_number = int(num_as_string[1])
    third_number = int(num_as_string[2])
    fourth_number = int(num_as_string[3])
    if first_number == 0 or second_number == 0 or third_number == 0 or fourth_number == 0:
        continue
    if number % first_number == 0 \
            and number % second_number == 0 \
            and number % third_number == 0 \
            and number % fourth_number == 0:
        is_special = True
        print(i, end=" ")
