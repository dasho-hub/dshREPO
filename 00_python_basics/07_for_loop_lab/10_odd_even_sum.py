input_count = int(input())

sum_of_even_numbers = 0
sum_of_odd_numbers = 0

for number in range(0, input_count):
    current_number = int(input())
    if number % 2 == 0:
        sum_of_even_numbers += current_number
    else:
        sum_of_odd_numbers += current_number

if sum_of_even_numbers == sum_of_odd_numbers:
    print(f"Yes\nSum = {sum_of_even_numbers}")
else:
    print(f"No\nDiff = {abs(sum_of_even_numbers - sum_of_odd_numbers)}")