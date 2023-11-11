import math

the_number = int(input())
combo_found = False

the_number_str = str(the_number)
last_digit = int(the_number_str[2])
combination = 0


for a in range(1, 9 + 1):
    if combination != 0:
        break
    for b in range(9, a, -1):
        if combination != 0:
            break
        for c in range(0, 9):
            if combination != 0:
                break
            for d in range(9, c, -1):
                first_condition = math.floor((a * b * c * d) / (a + b + c + d))
                second_condition = (the_number % 3 == 0)
                if first_condition == 3 and second_condition:
                    combination = str(d) + str(c) + str(b) + str(a)
                    combo_found = True
                    print(combination)
                    break
                if (a + b + c + d) == (a * b * c * d) and last_digit == 5:
                    combination = str(a) + str(b) + str(c) + str(d)
                    combo_found = True
                    print(combination)
                    break
if combination == 0:
    print("Nothing found")
