target = int(input())
sum_of_inputs = 0

while sum_of_inputs < target:
    ask_for_new_number = int(input())
    sum_of_inputs += ask_for_new_number

print(sum_of_inputs)