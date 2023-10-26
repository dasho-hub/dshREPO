input_count = int(input())

sum_of_left_numbers = 0
sum_of_right_numbers = 0

for number in range(2 * input_count):
    if number < input_count:
        current_number = int(input())
        sum_of_left_numbers += current_number
    else:
        sum_of_right_numbers += int(input())

if sum_of_left_numbers == sum_of_right_numbers:
    print(f"Yes, sum = {sum_of_left_numbers}")
else:
    print(f"No, diff = {abs(sum_of_left_numbers - sum_of_right_numbers)}")