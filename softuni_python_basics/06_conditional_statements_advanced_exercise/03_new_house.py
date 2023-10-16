flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    if flower_count <= 80:
        price = 5
    else:
        price = (5 - (5 * 0.1))
elif flower_type == "Dahlias":
    if flower_count <= 90:
        price = 3.8
    else:
        price = (3.8 - (3.8 * 0.15))
elif flower_type == "Tulips":
    if flower_count <= 80:
        price = 2.8
    else:
        price = (2.8 - (2.8 * 0.15))
elif flower_type == "Narcissus":
    if flower_count < 120:
        price = (3 + (3 * 0.15))
    else:
        price = 3
elif flower_type == "Gladiolus":
    if flower_count < 80:
        price = (2.5 + (2.5 * 0.2))
    else:
        price = 2.5
else:
    pass

if budget >= (flower_count * price):
    money_left = budget - (flower_count * price)
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
else:
    money_left = (flower_count * price) - budget
    print(f"Not enough money, you need {money_left:.2f} leva more.")