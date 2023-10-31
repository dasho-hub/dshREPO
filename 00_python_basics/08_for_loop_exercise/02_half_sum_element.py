import sys

input_count = int(input())
sum_of_numbers = 0
max_num = -sys.maxsize

for _ in range(input_count):
    current_number = int(input())
    sum_of_numbers += current_number
    if current_number > max_num:
        max_num = current_number


rest_sum = sum_of_numbers - max_num
if max_num == rest_sum:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - rest_sum)
    print("No")
    print(f"Diff = {diff}")