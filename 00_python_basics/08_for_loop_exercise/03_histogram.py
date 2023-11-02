number_of_inputs = int(input())
p1_percent = 0
p2_percent = 0
p3_percent = 0
p4_percent = 0
p5_percent = 0

for _ in range(number_of_inputs):
    current_number = int(input())
    if current_number < 200:
        p1_percent += 1
    elif 200 <= current_number < 400:
        p2_percent += 1
    elif 400 <= current_number < 600:
        p3_percent += 1
    elif 600 <= current_number < 800:
        p4_percent += 1
    else:
        p5_percent += 1

first_percent = p1_percent / number_of_inputs * 100
second_percent = p2_percent / number_of_inputs * 100
third_percent = p3_percent / number_of_inputs * 100
fourth_percent = p4_percent / number_of_inputs * 100
fifth_percent = p5_percent / number_of_inputs * 100

print(f"{first_percent:.2f}%")
print(f"{second_percent:.2f}%")
print(f"{third_percent:.2f}%")
print(f"{fourth_percent:.2f}%")
print(f"{fifth_percent:.2f}%")